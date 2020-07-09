from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import MeetingOut, MeetingIn, MeetingUpdate
from app.api import db_manager
from app.api.service import is_participant_present

meetings = APIRouter()


@meetings.post('/', response_model=MeetingOut, status_code=201)
async def create_meeting(payload: MeetingIn):
    for participant_id in payload.participants_id:
        if not is_participant_present(participant_id):
            raise HTTPException(status_code=404, detail=f"Participant with id:{participant_id} not found")

    meeting_id = await db_manager.add_meeting(payload)
    response = {
        'id': meeting_id,
        **payload.dict()
    }

    return response


@meetings.get('/', response_model=List[MeetingOut])
async def get_meetings():
    return await db_manager.get_all_meetings()


@meetings.get('/{id}/', response_model=MeetingOut)
async def get_meeting(id: int):
    meeting = await db_manager.get_meeting(id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting


@meetings.put('/{id}/', response_model=MeetingOut)
async def update_meeting(id: int, payload: MeetingUpdate):
    meeting = await db_manager.get_meeting(id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")

    update_data = payload.dict(exclude_unset=True)

    if 'participants_id' in update_data:
        for participant_id in payload.participants_id:
            if not is_participant_present(participant_id):
                raise HTTPException(status_code=404, detail=f"Participant with given id:{participant_id} not found")

    meeting_in_db = MeetingIn(**meeting)

    updated_meeting = meeting_in_db.copy(update=update_data)

    return await db_manager.update_meeting(id, updated_meeting)


@meetings.delete('/{id}', response_model=None)
async def delete_meeting(id: int):
    meeting = await db_manager.get_meeting(id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return await db_manager.delete_meeting(id)


@meetings.get('/user/{id}/', response_model=List[MeetingOut])
async def get_user_meetings(id: int):
    return await db_manager.get_user_meetings(id)
