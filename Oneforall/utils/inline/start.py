import random
from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle
import config
from Oneforall import app

# Premium Stickers ki list
STICKERS = [
    6312260233171312151, 5433824103134530018, 5431445213233261748, 
    5431718873433095333, 5443003051411513631, 5431634752706954211
]

def btn(text, style=ButtonStyle.DEFAULT, **kwargs):
    premium_id = random.choice(STICKERS)
    try:
        # Style parameter ko valid hona chahiye (PRIMARY, SUCCESS, WARNING, DANGER, ya DEFAULT)
        return InlineKeyboardButton(
            text=text,
            icon_custom_emoji_id=premium_id,
            style=style,
            **kwargs
        )
    except TypeError:
        return InlineKeyboardButton(text=text, **kwargs)

def start_panel(_):
    buttons = [
        [
            btn(_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.SUCCESS),
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.PRIMARY),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", style=ButtonStyle.SUCCESS)
        ],
        [
            btn("ᴇʀᴇɴ ʏᴇᴀɢᴇʀ", url="https://t.me/toxication_infinity", style=ButtonStyle.PRIMARY),
            # Yahan SECONDARY ki jagah maine PRIMARY rakha hai crash rokne ke liye
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=ButtonStyle.PRIMARY), 
        ],
        [
            btn(_["S_B_4"], callback_data="settings_back_helper", style=ButtonStyle.WARNING)
        ],
        [
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL, style=ButtonStyle.DANGER),
            btn(_["S_B_5"], url="https://t.me/docker_git_bit", style=ButtonStyle.PRIMARY)
        ],
        [
            btn("「 ⌯ ᴜᴘᴘєʀϻσσɴ ᴛᴜηєꜱ ⌯ 」", url="https://uppermooninfinity.jo3.org/", style=ButtonStyle.SUCCESS)
        ],
    ]
    return buttons
