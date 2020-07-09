from sqlalchemy import (Column, Integer, MetaData, String, Table, Boolean,
                        create_engine, ARRAY)
from sqlalchemy.dialects import postgresql
import os

from databases import Database

# DATABASE_URL = 'postgresql://meeting_user:meeting_password@localhost/meeting_db'
DATABASE_URL = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

meetings = Table(
    'meetings',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('group', String(50)),
    Column('participants_id', postgresql.ARRAY(Integer)),
    Column('owner', String(50)),
    Column('is_promoted', Boolean),
    Column('tags', ARRAY(String))
)

database = Database(DATABASE_URL)
