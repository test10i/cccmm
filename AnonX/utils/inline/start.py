from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=". aDD Me To Your Groups .",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=". aDD Me To Your Groups . ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="- Help .", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="- SUPPORT .", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="- BoT OWNER .", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="- Dev Source .", url=config.UPSTREAM_REPO
            )
        ],
     ]
    return buttons
