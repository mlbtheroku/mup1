import os


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "5625875943:AAHLbVYYvqITKgudHOSh0gfnOeKa7g5r7Kc"
    # The Telegram API things
    APP_ID = 17894641
    API_HASH = "4e5b39e5c7c6066e5144dfc50cf466cf"
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5468192421").split())
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", None)
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get(
        "DEF_THUMB_NAIL_VID_S", ""
    ) # https://placehold.it/90x90
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from
    # https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
    # database

    DATABASE_NAME = "LegendBot"
    DATABASE_URL = "mongodb+srv://AutoAnime:AutoAnime@autoanime.f8ahzhs.mongodb.net/?retryWrites=true&w=majority"
