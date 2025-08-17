from fastapi import APIRouter

router = APIRouter (
    prefix = "/stream",
    tags = ["Streams"]
)

# Routers (Endpoints) for all streams list.
@router.get("/search/{stream_title}")
def search_stream(stream_title: str):
    return f"Here's the stream with title: {stream_title}."