from bot import app
from bot.utils.utils import load_plugins

load_plugins()
print("Bot Imported All Plugins")
print("Bot Started Successfully")

if __name__ == "__main__":
    app.run_until_disconnected()
