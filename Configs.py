import os

class Config(object):
    TOKEN = os.environ.get("TOKEN", None)
    API_HASH = os.environ.get("API_HASH", None)
    API_ID = int(os.environ.get("API_ID", 6))
    CHANNEL_US = os.environ.get("CHANNEL_US", None)
    CHANNEL_URL = os.environ.get("CHANNEL_URL", None)
    LOGS_CHAT = int(os.environ.get("LOGS_CHAT", False))
