from fastapi import APIRouter

router = APIRouter (
    prefix = "/user",
    tags = ["Users"]
)

# Routers (Endpoints) for all streams list.
@router.get("/{streamer_id}")
def channel(streamer_id: int):
    return "Here's your channel streamer: Channel Link"