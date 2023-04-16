import requests


class SlavikAPIClient:
    def __init__(self, base_url: str, api_key: str, password: str = None):
        self.base_url = base_url
        if not self.base_url.endswith('/'):
            self.base_url += '/'
        self.api_key = api_key
        self.password = password
        self.headers = {
            'Content-Type': 'application/json',
        }

    def _get_url(self, endpoint):
        return f'{self.base_url}{self.api_key}{endpoint}'

    def _get(self, endpoint, params=None):
        response = requests.get(self._get_url(endpoint), headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint, data=None, json=None):
        response = requests.post(self._get_url(endpoint), headers=self.headers, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def get_userinfo(self):
        endpoint = '/get_userinfo'
        return self._get(endpoint)

    def create_action(self, soft, action):
        endpoint = '/new_action'
        return self._post(endpoint, json={'soft': soft, 'action': action})

    def cancel_action(self, action_id):
        raise NotImplementedError()
