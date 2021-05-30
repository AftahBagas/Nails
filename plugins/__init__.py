# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import time

from pyUltroid.dB import *
from pyUltroid.dB.core import *
from pyUltroid.functions.all import *
from pyUltroid.functions.broadcast_db import *
from pyUltroid.functions.gban_mute_db import *
from pyUltroid.functions.google_image import googleimagesdownload
from pyUltroid.functions.greetings_db import *
from pyUltroid.functions.sudos import *
from pyUltroid.functions.ytdl import *
from pyUltroid.utils import *

from strings import get_string

try:
    import glitch_me
except ModuleNotFoundError:
    os.system(
        "git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me"
    )


start_time = time.time()
ultroid_version = "v0.0.8"
OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id

List = []
Dict = {}
N = 0


def grt(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


_small_caps = [
    "ᴀ",
    "ʙ",
    "ᴄ",
    "ᴅ",
    "ᴇ",
    "ғ",
    "ɢ",
    "ʜ",
    "ɪ",
    "ᴊ",
    "ᴋ",
    "ʟ",
    "ᴍ",
    "ɴ",
    "ᴏ",
    "ᴘ",
    "ϙ",
    "ʀ",
    "s",
    "ᴛ",
    "ᴜ",
    "ᴠ",
    "ᴡ",
    "x",
    "ʏ",
    "ᴢ",
]

_monospace = [
    "𝚊",
    "𝚋",
    "𝚌",
    "𝚍",
    "𝚎",
    "𝚏",
    "𝚐",
    "𝚑",
    "𝚒",
    "𝚓",
    "𝚔",
    "𝚕",
    "𝚖",
    "𝚗",
    "𝚘",
    "𝚙",
    "𝚚",
    "𝚛",
    "𝚜",
    "𝚝",
    "𝚞",
    "𝚟",
    "𝚠",
    "𝚡",
    "𝚢",
    "𝚣",
    "𝙰",
    "𝙱",
    "𝙲",
    "𝙳",
    "𝙴",
    "𝙵",
    "𝙶",
    "𝙷",
    "𝙸",
    "𝙹",
    "𝙺",
    "𝙻",
    "𝙼",
    "𝙽",
    "𝙾",
    "𝙿",
    "𝚀",
    "𝚁",
    "𝚂",
    "𝚃",
    "𝚄",
    "𝚅",
    "𝚆",
    "𝚇",
    "𝚈",
    "𝚉",
]


KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]
