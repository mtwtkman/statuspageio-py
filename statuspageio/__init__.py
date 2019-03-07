import json
from typing import NewType, Dict
from enum import Enum

import requests
from requests.models import Response


ApiKey = NewType('ApiKey', str)
PageId = NewType('PageId', str)
Url = NewType('Url', str)
Headers = NewType('Headers', Dict[str, str])
Payload = NewType('Payload', Dict[str, str])
Name = NewType('Name', str)
Body = NewType('Body', str)


class IncidentStatus(Enum):
    investigating = 'investigating'
    identified = 'identified'
    monitoring = 'monitoring'
    resolved = 'resolved'


class StatuspageIO:
    API_ROOT = 'https://api.statuspage.io/v1/pages/'

    def __init__(self, api_key: ApiKey, page_id: PageId):
        self.api_key = api_key
        self.page_id = page_id

    @property
    def _incident_endpoint(self):
        return f'{self.API_ROOT}{self.page_id}/incidents.json'

    @property
    def _headers(self) -> Headers:
        return Headers({'Authorization': f'OAuth {self.api_key}'})

    def _post(self, url: Url, payload: Payload) -> Response:
        return requests.post(url, data=json.dumps(payload), headers=self._headers)

    def create_incident(self, name: Name, status: IncidentStatus, body: Body) -> Response:
        payload = {
            'incident': {
                'name': name,
                'status': status.value,
                'body': body,
            }
        }
        return self._post(self._incident_endpoint, payload)


if __name__ == '__main__':
    import os
    s = StatuspageIO(os.environ['API_KEY'], os.environ['PAGE_ID'])
    resp = s.create_incident('hoge', IncidentStatus.investigating, 'neko')

    import pdb; pdb.set_trace()
    print(0)

