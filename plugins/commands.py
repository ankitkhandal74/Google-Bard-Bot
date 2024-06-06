import os
from info import Config
import sys
import asyncio 
import requests as req
import httpx
import json
from pyrogram import Client, filters, enums
from urllib.parse import quote
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument
import time, datetime 
from database import db 
from pyrogram.errors import InputUserDeactivated, FloodWait, UserIsBlocked


@Client.on_message(filters.command(["start"]))
async def start(client, message):
        buttons = [[
                    InlineKeyboardButton('☆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ☆', url=f'http://telegram.me/Ihgfdryhcvbhhbot?startgroup=true')
                ],[
                   InlineKeyboardButton('😎🆒 Follow me on Instagram🆒😎', url=f'https://www.instagram.com/aye_nikhiil.07?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==')
                ]]
        reply_markup = InlineKeyboardMarkup(buttons)    
        m = await message.reply_sticker("CAACAgQAAxkBAAEKeqNlIpmeUoOEsEWOWEiPxPi3hH5q-QACbg8AAuHqsVDaMQeY6CcRojAE")
        await asyncio.sleep(1)
        await m.delete()
        PICS = "https://graph.org/file/9785bccb309971227eda8.jpg"
        START_TXT = f"Hello! Send me a message and I will respond."
        await message.reply_photo(
            photo=PICS,
            caption=START_TXT,
            reply_markup=reply_markup,
        )


@Client.on_message(filters.text)
async def message(client, message):
    user_text = message.text
    encoded_text = quote(user_text)  # URL-encode the user text
    full_url = f"https://chatgpt.apinepdev.workers.dev/?question={encoded_text}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(full_url)
            # Check if the request was successful
            if response.status_code == 200:
                # Extract response text from JSON
                data = response.json()
                response_text = data.get('answer', 'Sorry, something went wrong.')
                # Send the response text back to the user     
                m=await message.reply_sticker             ("CAACAgQAAxkBAAEKeqNlIpmeUoOEsEWOWEiPxPi3hH5q-QACbg8AAuHqsVDaMQeY6CcRojAE") 
                await asyncio.sleep(0.1)
                await m.delete()
                await message.reply_text(response_text)
            else:
                await message.reply_text("Sorry, something went wrong.")
    except httpx.RequestError as e:
        await message.reply_text("Sorry, something went wrong.")


