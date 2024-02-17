import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1002029882658')
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")
    mediaPattern = r"\b(https?://(?:(.*?)\.)?(?:instagram\.com|instagr\.am|t\.co|twitter\.com)(?:[^\s]*))\b" #pin\.it|pinterest\.com|
