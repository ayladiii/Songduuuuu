import os


class Config:

   API_ID = int(os.getenv("API_ID", "8953338"))
   API_HASH = os.getenv("API_HASH", "fe21f223cb02d8f7c1cbda651f553a45")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "2142897671:AAEHf0HdxZN3vm3eUcTz72dB38ma8vY_AaE")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "MusicAzBot")
   OWNER_ID = int(os.environ.get("OWNER_ID","5865605067"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Husidi") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001898638971"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "MusicAzPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001692410500"))
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "ef763571-688b-4eae-b8ac-4eeefaf23c48")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "HUSEYN")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/dc9794139c12507f5eb1c.jpg")    