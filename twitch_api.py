import requests
import os
import urllib

class TwitchApi:

    def __init__(self):
        self.headers = None
        self.AUTH_ENDPOINT: str = "https://id.twitch.tv/oauth2/token"
        self.CLIPS_ENDPOINT: str = "https://api.twitch.tv/helix/clips"
        self.USERS_ENDPOINT: str = "https://api.twitch.tv/helix/users"
        self.CLIPS_ENDPOINT: str = "https://api.twitch.tv/helix/clips"
    
    def authorize(self, client_id: str, client_secret: str):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = f'client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials'
        try:
            response = requests.post("https://id.twitch.tv/oauth2/token", headers=self.headers, data=data)
            if(response.ok):
                print("SESSION AUTHORIZED, token received.")
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
        bearer = response.json()['access_token']
        self.headers = {
            'Authorization' : f'Bearer {bearer}',
            'Client-Id' : client_id,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def get_user_id(self, name: str) -> str:
        try:
            name = name.lower()
            response = requests.get('https://api.twitch.tv/helix/users?login={}'.format(name.lower()), headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)

        broadcaster_id = response.json()['data'][0]['id']
        return broadcaster_id

    def get_clips_info(self, broadcaster_id: str, limit: int, start_date: str, end_date: str):
        try:
            response = requests.get('https://api.twitch.tv/helix/clips?broadcaster_id={}&first={}&started_at={}&ended_at={}'.format(broadcaster_id, limit, start_date, end_date), headers=self.headers,)
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)

    def download_clip(self, title, clip_url):
        mp4_url = clip_url.split("-preview", 1)[0] + ".mp4"
        r = requests.get(mp4_url)
        base_path = "tmp/"
        file_path = base_path + title + ".mp4"
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        try:
            urllib.request.urlretrieve(mp4_url, file_path)
            return file_path
        except Exception as err:
            print(err)





