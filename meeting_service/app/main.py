from fastapi import FastAPI

from app.api.meetings import meetings
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# app.include_router(meetings)
app.include_router(meetings, prefix='/api/v1/meetings', tags=['meetings'])
