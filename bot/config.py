from os import environ

class Config:
    api_id = environ.get("TG_ID", None)
    api_hash = environ.get("Tg_HASH", "")
    bot_token = environ.get("BOT_TOKEN", "")
