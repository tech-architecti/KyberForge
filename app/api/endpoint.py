import json
from http import HTTPStatus
from typing import Dict, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response, StreamingResponse

from api.event_stream_generator import event_stream_generator
from database.event import Event
from database.repository import GenericRepository
from database.session import db_session
from schemas.streaming_schema import StreamingSchema
from worker.config import celery_app
from workflows.streaming_example_workflow import StreamingExampleWorkflow
from workflows.workflow_registry import WorkflowRegistry
router = APIRouter()


@router.post("/streaming")
async def handle_chat_completion_streaming(
        data: StreamingSchema
) -> StreamingResponse:
    workflow = StreamingExampleWorkflow()
    workflow_stream = workflow.run_stream_async(data.model_dump())

    return StreamingResponse(
        event_stream_generator(workflow_stream),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.post("/", dependencies=[])
def handle_event(
        data: Any,
        session: Session = Depends(db_session),
) -> Response:
    repository = GenericRepository(
        session=session,
        model=Event,
    )
    raw_event = data.model_dump(mode="json")
    event = Event(data=raw_event, workflow_type=get_workflow_type(raw_event))
    repository.create(obj=event)

    task_id = celery_app.send_task(
        "process_incoming_event",
        args=[str(event.id)],
    )

    return Response(
        content=json.dumps({"message": f"process_incoming_event started `{task_id}` "}),
        status_code=HTTPStatus.ACCEPTED,
    )


def get_workflow_type(data: Dict) -> str:
    return WorkflowRegistry.PLACEHOLDER.name
