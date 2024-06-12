from info import *
from pyrogram import Client, filters
import os
import logging 
import logging.config
from plugins import *

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)



if __name__ == '__main__':
       plugins = dict(
        root="plugins"
    )


app = Client(
        "ShowJson",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100,
    )

    
app.run()
