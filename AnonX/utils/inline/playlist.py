from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=". PERSONAL .",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text=". GLOBAL .", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text=". CLOSK .", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=". ToP PLaYLisTs .", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text=". PERSONAL .", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text=". GLOBAL .", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text=". Groups .", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text=". BacK .", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text=". CLOSK .", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=". AuDio .", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text=". viDeo .", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text=". BacK .", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text=". CLOSK .", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=". ToP PLaYLisTs .", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text=". PERSONAL .", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text=". GLOBAL .", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text=". CLOSK .", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text=". BacK .", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text=". CLOSK .", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=". BacK .",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text=". CLOSK .", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=". DeLeLTe .",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=". BacK .",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text=". CLOSK .",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=". CLOSK .",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
