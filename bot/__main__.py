from bot import app
from bot.utils.utils import load_plugins
from bot.logging import LOG

if __name__ == "__main__":
    load_plugins()
    LOG.info("Bot Imported All Plugins")
    LOG.info("Bot Started Successfully")
    app.run_until_disconnected()
