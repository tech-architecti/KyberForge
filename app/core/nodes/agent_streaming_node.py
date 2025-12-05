from abc import ABC, abstractmethod
from typing import AsyncIterator, Dict, Any

from core.nodes.agent import AgentNode
from core.task import TaskContext
from utils.chunking_utils import ChunkingUtils


class AgentStreamingNode(AgentNode, ABC):
    def __init__(self, task_context: TaskContext = None):
        super().__init__(task_context=task_context)

    @abstractmethod
    async def process(self, task_context: TaskContext) -> AsyncIterator[Dict[str, Any]]:
        async with self.agent.run_stream("") as result:
            async for chunk in ChunkingUtils.stream_text_deltas(result):
                yield chunk
