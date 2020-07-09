from pydantic import BaseModel
from typing import List, Optional


class MeetingIn(BaseModel):
    name: str
    group: str
    participants_id: List[int]
    owner: str
    is_promoted: bool
    tags: List[str]


class MeetingOut(MeetingIn):
    id: int


class MeetingUpdate(MeetingIn):
    name: Optional[str] = None
    group: Optional[str] = None
    participants_id: Optional[List[int]] = None
    owner: Optional[str] = None
    is_promoted: Optional[bool] = None
    tags: Optional[List[str]] = None
