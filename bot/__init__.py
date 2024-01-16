from bot.config import Config

from telethon import TelegramClient


app = TelegramClient('anon', Config.api_id, Config.api_hash).start(bot_token=Config.bot_token)
