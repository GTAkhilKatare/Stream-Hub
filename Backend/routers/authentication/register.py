from fastapi import APIRouter

router = APIRouter (
    prefix = "/auth",
    tags = ["Authentication"],
)

# Routers (Endpoints) for register
@router.get("/register")
def get_register_page():
    return "You are onto register page."

@router.post("/register")
def register():
    pass