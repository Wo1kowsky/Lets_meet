import os
import httpx

USER_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/users/'
url = os.environ.get('USER_SERVICE_HOST_URL') or USER_SERVICE_HOST_URL


def is_participant_present(participant_id: int):
    r = httpx.get(f'{url}{participant_id}/')
    return True if r.status_code == 200 else False
