from typing import AsyncIterator, Dict, Any

from core.nodes.agent import AgentConfig
from core.nodes.agent_streaming_node import AgentStreamingNode
from core.task import TaskContext
from utils.chunking_utils import ChunkingUtils


class StreamingNode(AgentStreamingNode):
    def get_agent_config(self) -> AgentConfig:
        pass

    async def process(self, task_context: TaskContext) -> AsyncIterator[Dict[str, Any]]:
        async with self.agent.run_stream("") as result:
            async for chunk in ChunkingUtils.stream_text_deltas(result):
                yield chunk