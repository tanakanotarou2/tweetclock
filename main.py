import datetime
import os
import tempfile
from pathlib import Path

import pytz
import tweepy
from PIL import Image
from dotenv import load_dotenv

from draw_clock import draw_clock

load_dotenv()  # take environment variables from .env.

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

if __name__ == '__main__':
    api = tweepy.API(auth)

    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    img_path = Path("./imgs/base.jpg")
    im = Image.open(img_path)
    im = draw_clock(im, now, "red")
    with tempfile.NamedTemporaryFile() as f:
        im.save(f, "PNG")
        api.update_profile_image(f.name)
