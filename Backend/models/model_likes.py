from pydantic import BaseModel

class Likes(BaseModel):
    """A pydantic request model for like count."""

    stream_id: str
    user_id: str

class LikesResponse(Likes):
    """A pydantic response model for like count."""