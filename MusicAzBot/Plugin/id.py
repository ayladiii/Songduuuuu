# @MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə

from pyrogram.types import Message, User
from MusicAzBot import MusicAzBot as app
from MusicAzBot import LOGGER
from helpers.filters import command
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
import pyrogram
from pyrogram.errors import FloodWait
from MusicAzBot.config import Config
from datetime import datetime


@app.on_message(filters.command('id'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**Sənin ID**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ID**: `{reply.from_user.id}`\n**Söhbət ID**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**Sənin ID**: `{message.from_user.id}`\n**Söhbət ID**: `{message.chat.id}`"
        )