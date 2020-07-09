from app.api.models import MeetingIn, MeetingOut, MeetingUpdate
from app.api.db import meetings, database


async def add_meeting(payload: MeetingIn):
    query = meetings.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_meetings():
    query = meetings.select()
    return await database.fetch_all(query=query)


async def get_meeting(id):
    query = meetings.select(meetings.c.id == id)
    return await database.fetch_one(query=query)


async def delete_meeting(id: int):
    query = meetings.delete().where(meetings.c.id == id)
    return await database.execute(query=query)


async def update_meeting(id: int, payload: MeetingIn):
    query = (
        meetings
            .update()
            .where(meetings.c.id == id)
            .values(**payload.dict())
    )
    return await database.execute(query=query)


async def get_user_meetings(id: int):
    # query = meetings.select(meetings.c.participants_id.contains(id))
    query = meetings.select().where(meetings.c.participants_id.contains([id, ]))
    return await database.fetch_all(query=query)
