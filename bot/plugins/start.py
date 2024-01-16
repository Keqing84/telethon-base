from bot import app
from telethon import events, Button
from bot.utils.utils import BtCrt

@app.on(events.NewMessage(incoming=True, pattern="/start"))
async def _start(event):
    bt = BtCrt()
    bt.add_url("Test URl","https://t.mekai8_4")
    bt.add_callback("Inline Button", "checkss")
    await event.reply("Hello!, This Is A Test Bot Running In Telethon",
                    buttons=bt.btns
             )


@app.on(events.callbackquery.CallbackQuery(data="checkss"))
async def _callby(event):
    await event.edit("You clicked a button!")
