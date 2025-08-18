from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    """A pydantic request model for user or viewer data."""

    email: str
    username: str
    password: str
    user_type: Optional[str] = "viewer"

class UserResponse(BaseModel):
    """A user response model."""

    username: str