from fastapi import APIRouter

router = APIRouter (
    prefix = "/stream",
    tags = ["Streams"]
)

# Routers (Endpoints) for live stream.
@router.get("/live/{stream_id}")
def stream(stream_id: int):
    return f"Here's the stream with stream id: {stream_id}."