from pydantic import BaseModel


class StreamingSchema(BaseModel):
    message: str
