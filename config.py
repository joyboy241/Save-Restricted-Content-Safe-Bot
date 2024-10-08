# DEEPAK_JANGID
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "10758818"))
API_HASH = getenv("API_HASH", "04fbbf6e526799e099494e33c891aa95")
BOT_TOKEN = getenv("BOT_TOKEN", "7389306950:AAGsgk53l2GhihtPrhyFEYRckbcvKEbGnt0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1234819262").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://deepakjangidjoyboy:deepak!123@cluster0.vljsovf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1001680979427")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002473297204"))
