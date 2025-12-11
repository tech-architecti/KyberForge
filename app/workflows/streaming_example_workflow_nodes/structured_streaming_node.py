from typing import AsyncIterator, Dict, Any

from core.nodes.agent import AgentConfig, ModelProvider
from core.nodes.agent_streaming_node import AgentStreamingNode
from core.task import TaskContext
from schemas.streaming_example_schema import StreamingExampleSchema


class StructuredStreamingNode(AgentStreamingNode):
    class OutputType(AgentStreamingNode.OutputType):
        thinking: str
        reply: str

    def get_agent_config(self) -> AgentConfig:
        return AgentConfig(
            model_provider=ModelProvider.MISTRAL,
            model_name="mistral-small-2506",
            output_type=self.OutputType,
        )

    async def process(self, task_context: TaskContext) -> AsyncIterator[Dict[str, Any]]:
        event: StreamingExampleSchema = task_context.event
        async with self.agent.run_stream(user_prompt=event.message) as result:
            async for chunk in self.stream_structured_deltas(result):
                yield chunk
