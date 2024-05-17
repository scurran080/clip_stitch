import twitch_api
import os
from dotenv import load_dotenv

from stitch import stitch

load_dotenv()


class ClipStitch(object):
    def run(self, username, clip_limit, begin_year, begin_month, begin_day, end_year, end_month, end_day):
        api: twitch_api.TwitchApi = twitch_api.TwitchApi()
        api.authorize(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
        user_id = api.get_user_id(username)
        info = api.get_clips_info(user_id, clip_limit, f'{begin_year}-{begin_month}-{begin_day}T12:00:00-00:00',
                                  f'{end_year}-{end_month}-{end_day}T12:00:00-00:00')
        clip_paths = []
        for element in info['data']:
            file_url = element['thumbnail_url']
            file_title = element['title']
            path = api.download_clip(file_title, file_url)
            print(file_title + " DOWNLOADED.")
            clip_paths.append(path)
        stitch(clip_paths)
        print("VIDEO OUTPUT TO output.mp4.")
