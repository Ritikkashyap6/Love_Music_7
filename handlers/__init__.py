import re
import sys
import time
from config import (API_ID, API_HASH, BOT_TOKEN)

from pyrogram import Client

StartTime = time.time()

app = Client(
    "πββ π©ππππͺκͺΎπβ ββ¨π₯π»πππ_ππππππ₯β¨",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

