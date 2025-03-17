# © Coded by @Dypixx

import os

API_ID = os.getenv("API_ID", "29382018")
API_HASH = os.getenv("API_HASH", "4734a726c04620c61ec0a28a1ae0d57f")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8035534743:AAEoRY7p2i_MVMh2AJ4VgffFgjPuZKoLYGM")
ADMIN = int(os.getenv("ADMIN", "7442532306"))

CHNL_LINK = os.getenv("CHNL_LINK", "https://t.me/noob_project")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002428562251"))
DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1002428562251"))

DB_URI = os.getenv("DB_URI", "mongodb+srv://mrnoobx:DAZCdTczVWyECi04@cluster0.sedgwxy.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.getenv("DB_NAME", "instalaoder")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "-1002310978225") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH


"""
This code is created and owned by @Dypixx. Do not remove or modify the credit.

Removing the credit does not make you a developer; it only shows a lack of respect for real developers.
  
Respect the work. Keep the credit.

"""
