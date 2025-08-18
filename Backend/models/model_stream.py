from pydantic import BaseModel
from datetime import datetime

class Stream(BaseModel):
    """A pydantic request model for streams."""

    streamer_id: str
    title: str
    thumbnail_url: str
    stream_key: str
    likes: int

    rtmp_url: str
    hls_url: str
    recording_path: str

    started_at: datetime
    ended_at: datetime
    duration: str

class StreamResponse(BaseModel):
    """A pydantic response model for streams."""

    streamer_id: str
    title: str

    thumbnail_url: str
    likes: int

    hls_url: str
    started_at: datetime
    
    ended_at: datetime
    duration: str