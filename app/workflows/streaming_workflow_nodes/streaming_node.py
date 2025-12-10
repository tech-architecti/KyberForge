from typing import AsyncIterator, Dict, Any

from core.nodes.agent import AgentConfig, ModelProvider
from core.nodes.agent_streaming_node import AgentStreamingNode
from core.task import TaskContext


class StreamingNode(AgentStreamingNode):
    def get_agent_config(self) -> AgentConfig:
        return AgentConfig(
            model_provider=ModelProvider.MISTRAL,
            model_name="mistral-small-2506"
        )

    async def process(self, task_context: TaskContext) -> AsyncIterator[Dict[str, Any]]:
        async with self.agent.run_stream("Hey") as result:
            async for chunk in self.stream_text_deltas(result):
                yield chunk
