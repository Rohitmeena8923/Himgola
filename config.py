"""
from os import getenv


API_ID = int(getenv("API_ID", "27775431"))
API_HASH = getenv("API_HASH", "b70bb1d45a1d05236671d4cc615e40f9")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "6414266397"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6727160308").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://creatorar30:fdINvMPYXYwUyHdq@cluster0.pbaou.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-2446676469"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-2446676469"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "27775431"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6414266397"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6727160308").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-2446676469"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002446676469"))

