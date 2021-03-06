"""
AccGenBot
Copyright (C) 2021 TgxBotz

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

See < https://github.com/TgxBotz/AccGenBot/blob/master/LICENSE > 
for the license.
"""

import os
import logging
from telethon import TelegramClient
from Configs import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

bot = TelegramClient('AccGen', api_id=Config.API_ID, api_hash=Config.API_HASH)
AccGen = bot.start(bot_token=Config.TOKEN)
