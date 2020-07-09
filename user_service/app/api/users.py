from fastapi import APIRouter, HTTPException

from app.api.models import UserIn, UserUpdate, UserOut
from app.api import db_manager
from app.api.service import get_user_meetings

users = APIRouter()


@users.post('/', response_model=UserOut, status_code=201)
async def create_user(payload: UserIn):
    user_id = await db_manager.add_user(payload)

    response = {
        'id': user_id,
        **payload.dict()
    }

    return response


@users.get('/{id}/', response_model=UserOut)
async def get_user(id: int):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users.get('/{id}/meetings/')
async def get_meetings(id: int):
    meetings = get_user_meetings(id)

    response = {
        'id': id,
        'meetings': meetings
    }

    return response
