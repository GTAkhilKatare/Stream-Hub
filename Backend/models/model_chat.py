from pydantic import BaseModel

class Chats(BaseModel):
    """A pydantic request model for chats."""

    stream_id: str
    user_id: str
    message: str

class ChatsResponse(Chats):
    """A pydantic response model for chats."""