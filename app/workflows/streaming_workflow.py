from core.schema import WorkflowSchema, NodeConfig
from core.workflow import Workflow
from schemas.streaming_schema import StreamingSchema
from workflows.streaming_workflow_nodes.streaming_node import StreamingNode


class StreamingWorkflow(Workflow):
    workflow_schema = WorkflowSchema(
        description="",
        event_schema=StreamingSchema,
        start=StreamingNode,
        nodes=[
            NodeConfig(
                node=StreamingNode,
                connections=[],
                description="",
            ),
        ],
    )
