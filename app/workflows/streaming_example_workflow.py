from core.schema import WorkflowSchema, NodeConfig
from core.workflow import Workflow
from schemas.streaming_example_schema import StreamingExampleSchema
from workflows.streaming_example_workflow_nodes.structured_streaming_node import (
    StructuredStreamingNode,
)
from workflows.streaming_example_workflow_nodes.text_streaming_node import (
    TextStreamingNode,
)


class StreamingExampleWorkflow(Workflow):
    workflow_schema = WorkflowSchema(
        description="",
        event_schema=StreamingExampleSchema,
        start=TextStreamingNode,
        nodes=[
            NodeConfig(
                node=TextStreamingNode,
                connections=[StructuredStreamingNode],
                description="",
            ),
            NodeConfig(
                node=StructuredStreamingNode,
                connections=[],
                description="",
            ),
        ],
    )
