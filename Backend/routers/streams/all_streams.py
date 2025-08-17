from fastapi import APIRouter

router = APIRouter (
    prefix = "/stream",
    tags = ["Streams"]
)

# Routers (Endpoints) for all streams list.
@router.get("/all-streams")
def all_streams():
    return "Here is the list of all streams."