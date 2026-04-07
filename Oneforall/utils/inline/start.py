import random
from pyrogram.types import InlineKeyboardButton
# ButtonStyle ko import karne ki zaroorat nahi agar hum direct value use karein
import config
from Oneforall import app

# Premium Stickers IDs
STICKERS = [
    6312260233171312151, 5433824103134530018, 5431445213233261748, 
    5431718873433095333, 5443003051411513631, 5431634752706954211
]

def btn(text, style=None, **kwargs):
    """
    Style values for Pyrogram:
    1 = PRIMARY (Blue)
    2 = SUCCESS (Green)
    3 = WARNING (Orange/Yellow)
    4 = DANGER (Red)
    """
    premium_id = random.choice(STICKERS)
    try:
        return InlineKeyboardButton(
            text=text,
            icon_custom_emoji_id=premium_id,
            style=style, # Direct integer pass hoga yahan
            **kwargs
        )
    except TypeError:
        return InlineKeyboardButton(text=text, **kwargs)

def start_panel(_):
    buttons = [
        [
            btn(_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", style=2), # SUCCESS
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=1), # PRIMARY
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", style=2) # SUCCESS
        ],
        [
            btn("ᴇʀᴇɴ ʏᴇᴀɢᴇʀ", url="https://t.me/toxication_infinity", style=1),
            btn(_["S_B_2"], url=config.SUPPORT_CHAT, style=1), 
        ],
        [
            # Yahan WARNING (3) crash kar raha tha, ab fix hai
            btn(_["S_B_4"], callback_data="settings_back_helper", style=3) 
        ],
        [
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL, style=4), # DANGER
            btn(_["S_B_5"], url="https://t.me/docker_git_bit", style=1)
        ],
        [
            btn("「 ⌯ ᴜᴘᴘєʀϻσσɴ ᴛᴜηєꜱ ⌯ 」", url="https://uppermooninfinity.jo3.org/", style=2)
        ],
    ]
    return buttons
