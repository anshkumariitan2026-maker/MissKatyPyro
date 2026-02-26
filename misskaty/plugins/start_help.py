"""
* @author        yasir <yasiramunandar@gmail.com>
* @date          2022-12-01 09:12:27
* @projectName   MissKatyPyro
* Copyright @YasirPedia All rights reserved
"""
import contextlib
import re

from pyrogram import Client, filters
from pyrogram.errors import ChatSendPhotosForbidden, ChatWriteForbidden, QueryIdInvalid
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from misskaty import BOT_NAME, BOT_USERNAME, HELPABLE, app
from misskaty.helper import bot_sys_stats, paginate_modules
from misskaty.helper.localization import use_chat_lang
from misskaty.vars import COMMAND_HANDLER

home_keyboard_pm = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="˹ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅ˼", callback_data="bot_commands"),
            InlineKeyboardButton(
                text="˹sᴜᴘᴘᴏʀᴛ˼",
                url="https://t.me/ll_CarelessxCoder_ll",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sʏsᴛᴇᴍ sᴛᴀᴛs˼",
                callback_data="stats_callback",
            ),
            InlineKeyboardButton(text="˹ᴏᴡɴᴇʀ˼", url="tg://openmessage?user_id=8275132868"),
        ],
        [
            InlineKeyboardButton(
                text="˹ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ˼",
                url=f"http://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
    ]
)

home_text_pm = f"""
✨ ʜᴇʏ ᴛʜᴇʀᴇ, 🤍

➤ ɪ’ᴍ ˹𝐊єʟʟʏ ꭙ 𝐌ᴀɴᴀɢᴇєᴍєɴᴛ˼ , ʏᴏᴜʀ sᴍᴀʀᴛ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴀssɪsᴛᴀɴᴛ ⚡
ᴊᴜsᴛ ᴏɴᴇ ʙᴏᴛ… ʙᴜᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ғᴜɴ, ᴛᴏᴏʟs & ᴀɪ 😏

╭──〔 🌟 ᴡʜʏ ᴍᴇ? 〕──╮
➤ ᴀᴅᴍɪɴ ᴘᴏᴡᴇʀs ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ 👮
➤ sᴍᴀʀᴛ ᴀɪ ᴄʜᴀᴛ & ᴜᴛɪʟɪᴛʏ ᴛᴏᴏʟs 🤖
➤ ᴅᴏᴡɴʟᴏᴀᴅᴇʀs, sᴛɪᴄᴋᴇʀs & ғᴜɴ 🎧
➤ 30+ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴏɴᴇ 💎
╰────────────────╯
➤ ᴛʏᴘᴇ /help ᴀɴᴅ ᴇxᴘʟᴏʀᴇ ᴍʏ ᴘᴏᴡᴇʀs 🔥
"""
keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="˹ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅ˼", url=f"t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton(
                text="˹sᴜᴘᴘᴏʀᴛ˼",
                url="https://t.me/ll_CarelessxCoder_ll",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sʏsᴛᴇᴍ sᴛᴀᴛs˼",
                callback_data="stats_callback",
            ),
            InlineKeyboardButton(text="˹ᴏᴡɴᴇʀ˼", url="tg://openmessage?user_id=8275132868"),
        ],
    ]
)

FED_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Fed Owner Commands", callback_data="fed_owner"),
            InlineKeyboardButton("Fed Admin Commands", callback_data="fed_admin"),
        ],
        [
            InlineKeyboardButton("User Commands", callback_data="fed_user"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="help_back"),
        ],
    ]
)


@app.on_message(filters.command("start", COMMAND_HANDLER))
@use_chat_lang()
async def start(self, ctx: Message, strings):
    if ctx.chat.type.value != "private":
        nama = ctx.from_user.mention if ctx.from_user else ctx.sender_chat.title
        try:
            return await ctx.reply_photo(
                photo="https://files.catbox.moe/btthv2.jpg",
                caption=strings("start_msg").format(kamuh=nama),
                reply_markup=keyboard,
            )
        except (ChatSendPhotosForbidden, ChatWriteForbidden):
            return await ctx.chat.leave()
    if len(ctx.text.split()) > 1:
        name = (ctx.text.split(None, 1)[1]).lower()
        if "_" in name:
            module = name.split("_", 1)[1]
            text = (
                strings("help_name").format(mod=HELPABLE[module].__MODULE__)
                + HELPABLE[module].__HELP__
            )
            await ctx.reply_msg(
                text,
                disable_web_page_preview=True,
                message_effect_id=5104841245755180586,
            )
            if module == "federation":
                return await ctx.reply(
                    text=text,
                    reply_markup=FED_MARKUP,
                    disable_web_page_preview=True,
                    message_effect_id=5104841245755180586,
                )
            await ctx.reply(
                text,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("back", callback_data="help_back")]]
                ),
                disable_web_page_preview=True,
                message_effect_id=5104841245755180586,
            )
        elif name == "help":
            text, keyb = await help_parser(ctx.from_user.first_name)
            await ctx.reply_msg(
                text, reply_markup=keyb, message_effect_id=5104841245755180586
            )
    else:
        await self.send_photo(
            ctx.chat.id,
            photo="https://files.catbox.moe/btthv2.jpg",
            caption=home_text_pm,
            reply_markup=home_keyboard_pm,
            reply_to_message_id=ctx.id,
            message_effect_id=5104841245755180586,
        )


@app.on_callback_query(filters.regex("bot_commands"))
async def commands_callbacc(_, cb: CallbackQuery):
    text, keyb = await help_parser(cb.from_user.mention)
    await app.send_message(
        cb.message.chat.id,
        text=text,
        reply_markup=keyb,
        message_effect_id=5104841245755180586,
    )
    await cb.message.delete_msg()


@app.on_callback_query(filters.regex("stats_callback"))
async def stats_callbacc(_, cb: CallbackQuery):
    text = await bot_sys_stats()
    with contextlib.suppress(QueryIdInvalid):
        await app.answer_callback_query(cb.id, text, show_alert=True)


@app.on_message(filters.command("help", COMMAND_HANDLER))
@use_chat_lang()
async def help_command(_, ctx: Message, strings):
    if ctx.chat.type.value != "private":
        if len(ctx.command) >= 2:
            name = (ctx.text.split(None, 1)[1]).replace(" ", "_").lower()
            if str(name) in HELPABLE:
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=strings("click_me"),
                                url=f"t.me/{BOT_USERNAME}?start=help_{name}",
                            )
                        ],
                    ]
                )
                await ctx.reply_msg(
                    strings("click_btn").format(nm=name),
                    reply_markup=key,
                )
            else:
                await ctx.reply_msg(strings("pm_detail"), reply_markup=keyboard)
        else:
            await ctx.reply_msg(strings("pm_detail"), reply_markup=keyboard)
    elif len(ctx.command) >= 2:
        name = (ctx.text.split(None, 1)[1]).replace(" ", "_").lower()
        if str(name) in HELPABLE:
            text = (
                strings("help_name").format(mod=HELPABLE[name].__MODULE__)
                + HELPABLE[name].__HELP__
            )
            await ctx.reply_msg(
                text,
                disable_web_page_preview=True,
                message_effect_id=5104841245755180586,
            )
        else:
            text, help_keyboard = await help_parser(ctx.from_user.first_name)
            await ctx.reply_msg(
                text,
                reply_markup=help_keyboard,
                disable_web_page_preview=True,
                message_effect_id=5104841245755180586,
            )
    else:
        text, help_keyboard = await help_parser(ctx.from_user.first_name)
        await ctx.reply_msg(
            text,
            reply_markup=help_keyboard,
            disable_web_page_preview=True,
            message_effect_id=5104841245755180586,
        )


async def help_parser(name, keyb=None):
    if not keyb:
        keyb = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """💗 Hᴇʟʟᴏ 👋, Mʏ ɴᴀᴍᴇ ɪs {bot_name}. 

➤ I'ᴍ ᴀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs. Yᴏᴜ ᴄᴀɴ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ ʙᴏᴛ ᴜsɪɴɢ /setlang ᴄᴏᴍᴍᴀɴᴅ, ʙᴜᴛ ɪᴛ's sᴛɪʟʟ ɪɴ ʙᴇᴛᴀ sᴛᴀɢᴇ.
➤ Yᴏᴜ ᴄᴀɴ ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ, ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴀ ʙᴜᴛᴛᴏɴ.
""".format(
            first_name=name,
            bot_name="˹ᴋᴇʟʟʏ ꭙ ᴍᴀɴᴀɢᴇʀ˼",
        ),
        keyb,
    )


@app.on_callback_query(filters.regex(r"help_(.*?)"))
@use_chat_lang()
async def help_button(self: Client, query: CallbackQuery, strings):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = strings("help_txt").format(
        kamuh=query.from_user.first_name, bot=self.me.first_name
    )
    if mod_match:
        module = mod_match[1].replace(" ", "_")
        text = (
            strings("help_name").format(mod=HELPABLE[module].__MODULE__)
            + HELPABLE[module].__HELP__
        )
        if module == "federation":
            return await query.message.edit(
                text=text,
                reply_markup=FED_MARKUP,
                disable_web_page_preview=True,
            )
        await query.message.edit_msg(
            text=text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(strings("back_btn"), callback_data="help_back")]]
            ),
            disable_web_page_preview=True,
        )
    elif home_match:
        await app.send_msg(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=home_keyboard_pm,
        )
        await query.message.delete_msg()
    elif prev_match:
        curr_page = int(prev_match[1])
        await query.message.edit_msg(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match[1])
        await query.message.edit_msg(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit_msg(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help")),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyb = await help_parser(query)
        await query.message.edit_msg(
            text=text,
            reply_markup=keyb,
            disable_web_page_preview=True,
        )

    try:
        await self.answer_callback_query(query.id)
    except:
        pass
