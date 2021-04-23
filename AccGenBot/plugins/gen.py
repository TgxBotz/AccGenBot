from AccGenBot import AccGen
from AccGenBot.verify import verify
from telethon import events, Button
from Configs import Config

@AccGen.on(events.callbackquery.CallbackQuery(data="gen"))
async def gen(gen):
     check = await verify(Config.CHANNEL_US, gen, AccGen)
     if check is False:
       await event.reply("**Join my channel to use me:)**", buttons=[
       [Button.url("Join Channel", "{}".format(Config.CHANNEL_URL))]
       ])
     TEXT = """
**Heya {}**
Choose the account you wanna generate.
""".format(gen.sender.first_name)

     await gen.edit(TEXT, buttons=[
     [Button.inline("Zee5", data="zee5"), Button.inline("Voot", data="voot")],
     [Button.inline("AltBalaji", data="alt"), Button.inline("Spotify", data="sp")],
     [Button.url("My Source Code", "https://GitHub.com/TgxBotz/AccGenBot")]
     ])
