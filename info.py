import os
import re

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      API_ID = int(os.environ.get("API_ID", ""))
      API_HASH = os.environ.get("API_HASH", "")
      OWNER_ID = int(os.environ.get("OWNER_ID", ""))
      DB_URL = os.environ.get("DB_URL", "")
      DB_NAME = os.environ.get("DB_NAME", "")
      OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY', "")
      

api_url = "https://chatgpt.apinepdev.workers.dev/?question="
AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", ""))
# MongoDB information
DATABASE_URI = os.environ.get('DATABASE_URI', "")
DATABASE_NAME = os.environ.get('DATABASE_NAME', "")
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Telegram_files')
OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY', "")