from fastapi import APIRouter
from starlette.responses import StreamingResponse

from schemas.openai_schema import OpenaiChatSchema
from utils.event_stream_generator import event_stream_generator
from workflows.streaming_example_workflow import StreamingExampleWorkflow

router = APIRouter()


@router.post("/chat/completions", dependencies=[])
async def handle_chat_completion_streaming(
        data: OpenaiChatSchema
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
