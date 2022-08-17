import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "11792103")
    API_HASH = getenv("API_HASH", "5a03ee0c82de3e8972dd46a66e039b01")
    TOKEN = getenv("TOKEN", "2144094143:AAGKN04VmQ2hkXV_DDMJunjIDEFEOp704hA")
    OWNER_ID = getenv("OWNER_ID,"868753606")
    STRING_SESSION = getenv("STRING_SESSION", "BQBh78NSG_MoF7EEhBhsgJ1lsu1kr4osRxEL0iXLA8NlCUyYeQNiZhIbeNmfvsNn5ZMz7obXDXbSCNkh8ubhdDJkSWvVTQwaXrB2sIy2wrYpzkWqlruQ9z4tBMgcLMPskMbXtZ0QVGlAmOVGLq5tP2s_UIP01vP5WgyduIsXiMNYBl9S3dGx8gnOHSMnoi6jCCNwX4SFFSgAax-kicMZXj1PDYIGfgJuI6NRTuYDqj_sWAq6iPM3Dt7qKig7AOU7zVHDbVfutSDHBsflMa6vOoHCuBbCPbfbTHb6rsBp8cggg5nYUu_2wFnP4z5u5pmPHTtUVJo1i4rIlRtfCoFOUhfjU1QFhQA")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "smart_aruney")
    DB_URI = getenv("DATABASE_URL", "")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001645899463")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001645899463")
    SYS_ADMIN = getenv("SYS_ADMIN", "1669178360")
    DEV_USERS = getenv("DEV_USERS", "1669178360")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
