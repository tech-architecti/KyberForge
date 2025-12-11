from pydantic import BaseModel


class StreamingExampleSchema(BaseModel):
    message: str
