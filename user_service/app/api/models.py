from pydantic import BaseModel
from typing import Optional


class UserIn(BaseModel):
    name: str
    email: str = None


class UserOut(UserIn):
    id: int


class UserUpdate(UserIn):
    name: Optional[str] = None
