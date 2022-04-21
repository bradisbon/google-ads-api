import os
import requests

from google_ads_api.constants import CREDENTIALS_PATH, MCC_ID

import aiohttp
import yaml

def load_credentials():
    with open(os.path.expanduser(CREDENTIALS_PATH), 'r') as f:
        ads_yaml = yaml.load(f.read(),Loader=yaml.FullLoader)
    return ads_yaml


def refresh_token():
    creds = load_credentials()
    client_id = creds['adwords']['client_id']
    client_secret=creds['adwords']['client_secret']
    refresh_token=creds['adwords']['refresh_token']
    r = requests.post('https://www.googleapis.com/oauth2/v4/token',
                      data={'client_id':client_id,
                            'client_secret':client_secret,
                            'refresh_token':refresh_token,
                            'grant_type':'refresh_token'})
    return r.json()['access_token']


ACCESS_TOKEN = refresh_token()


class SessionManager():
    def __init__(self):
        self.access_token = ACCESS_TOKEN
        self.dev_token = load_credentials()['adwords']['developer_token']
        self._http_session: aiohttp.ClientSession

    async def __aenter__(self) -> aiohttp.ClientSession:
        self._http_session = aiohttp.ClientSession(headers = {
                'Content-Type': 'application/json',
                'developer-token': self.dev_token,
                'login-customer-id': MCC_ID,
                'Authorization': f"Bearer {self.access_token}",
            })
        return self._http_session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._http_session.close()

