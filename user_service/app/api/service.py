import os
import httpx

MEETING_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/meetings/'
url = os.environ.get('MEETING_SERVICE_HOST_URL') or MEETING_SERVICE_HOST_URL


def get_user_meetings(participant_id: int):
    r = httpx.get(f'{url}user/{participant_id}/')
    return r.json()
