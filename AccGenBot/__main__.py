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


import glob
from pathlib import Path
from AccGenBot.utils import load_plugins
import logging
from AccGenBot import AccGen

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "AccGenBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully Started AccGenBot!")
print("Visit @TgxBots")

if __name__ == "__main__":
    AccGen.run_until_disconnected()
