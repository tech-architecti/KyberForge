from typing import AsyncIterator


class ChunkingUtils:
    @staticmethod
    def completion_chunk(content: str) -> dict:
        return {
            "object": "chat.completion.chunk",
            "model": "default",
            "choices": [
                {
                    "index": 0,
                    "delta": {"role": "assistant", "content": content},
                    "finish_reason": None,
                }
            ],
        }

    @staticmethod
    async def stream_text_deltas(
            stream_result,
            debounce_by: float = 0.01,
    ) -> AsyncIterator[dict]:
        previous_text = ""
        async for text_chunk in stream_result.stream_text(debounce_by=debounce_by):
            if text_chunk.startswith(previous_text):
                delta_text = text_chunk[len(previous_text):]
            else:
                delta_text = text_chunk
            if not delta_text:
                continue
            previous_text = text_chunk
            yield ChunkingUtils.completion_chunk(delta_text)
