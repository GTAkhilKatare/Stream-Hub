from fastapi import APIRouter

router = APIRouter (
    prefix = "/user",
    tags = ["Users"]
)

# Routers (Endpoints) for all streams list.
@router.get("/{user_id}")
def profile(user_id: str):
    return "Here's your profile user."