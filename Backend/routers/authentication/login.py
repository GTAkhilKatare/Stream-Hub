from fastapi import APIRouter

router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"],
)

# Routes (Endpoints) for login
@router.get("/login")
def get_login_page():
    return "You are on login page."

@router.post("/login")
def login():
    pass