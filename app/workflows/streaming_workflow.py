from core.schema import WorkflowSchema, NodeConfig
from core.workflow import Workflow
from schemas.placeholder_schema import PlaceholderEventSchema
from workflows.streaming_workflow_nodes.streaming_node import StreamingNode


class PlaceholderWorkflow(Workflow):
    workflow_schema = WorkflowSchema(
        description="",
        event_schema=PlaceholderEventSchema,
        start=StreamingNode,
        nodes=[
            NodeConfig(
                node=StreamingNode,
                connections=[],
                description="",
            ),
        ],
    )
