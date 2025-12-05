import json
from typing import AsyncIterator


async def event_stream_generator(workflow_stream: AsyncIterator) -> AsyncIterator[str]:
    import logging

    try:
        event_count = 0
        async for event in workflow_stream:
            event_count += 1
            sse_data = f"data: {json.dumps(event)}\n\n"
            logging.info(f"SSE Event #{event_count}: {event.get('type', 'unknown')}")
            logging.info(sse_data)
            yield sse_data
        logging.info(f"Stream completed. Total events: {event_count}")
    except Exception as e:
        logging.error(f"Error in event_stream_generator: {e}", exc_info=True)
        error_event = {"type": "error", "error": str(e)}
        yield f"data: {json.dumps(error_event)}\n\n"
        raise
