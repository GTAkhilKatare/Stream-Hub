from pydantic import BaseModel
from typing import Optional

class Streamer(BaseModel):
    """A pydantic request model for streamer data."""

    user_id: str
    channel_name: str
    profile_pic: str # Path to the file.
    description: Optional[str] = None

class StreamerResponse(Streamer):
    """A pydantic response model for streamer data."""  