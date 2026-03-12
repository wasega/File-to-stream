# config.py (UPDATED)

import os
from dotenv import load_dotenv

load_dotenv(".env")

class Config:
    API_ID = int(os.environ.get("29895586", 0))
    API_HASH = os.environ.get("2e38dc8c9b16e0ae5890a6cae024b7d8", "")
    BOT_TOKEN = os.environ.get("8611954505:AAGC5H_tomX01BnyUTWnTMrvZlGz2FSV9gY", "")
    OWNER_ID = int(os.environ.get("1170382284", 0))
    
    _storage_channel_str = os.environ.get("-1003290832112")
    if _storage_channel_str:
        try: STORAGE_CHANNEL = int(_storage_channel_str)
        except ValueError: STORAGE_CHANNEL = _storage_channel_str
    else: STORAGE_CHANNEL = 0
    
    BASE_URL = os.environ.get("https://file-to-stream-g4qi.onrender.com", "").rstrip('/')
    DATABASE_URL = os.environ.get("mongodb+srv://waserecords:123bubu123@cluster0.vty48ho.mongodb.net/?appName=Cluster0", "")
    REDIRECT_BLOGGER_URL = os.environ.get("REDIRECT_BLOGGER_URL", "")
    BLOGGER_PAGE_URL = os.environ.get("BLOGGER_PAGE_URL", "")
    
    # --- YAHAN BADLAV KIYA GAYA HAI ---
    # Force Subscribe ke liye channel ID/username
    _fsub_channel_str = os.environ.get("FORCE_SUB_CHANNEL")
    if _fsub_channel_str:
        try: FORCE_SUB_CHANNEL = int(_fsub_channel_str)
        except ValueError: FORCE_SUB_CHANNEL = _fsub_channel_str
    else: FORCE_SUB_CHANNEL = 0
        
    # Yeh bot ka username store karega (code isse automatic set karega)
    BOT_USERNAME = "@bu_file_bot"
