from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 11057906))
API_HASH = getenv("API_HASH", "b7f975dcdf30c826b3e6178ff3f72356")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", 6864201346))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "TG_NAME_STYLE")
UPDATE_CHNL = getenv("UPDATE_CHNL", "TKS_JOIN")
OWNER_USERNAME = getenv("OWNER_USERNAME", "rainbow_dragonn")

# Random Start Images
IMG = [
    "https://telegra.ph/file/870bbc6b040bf757b849c.png",
]


# Random Stickers
STICKER = [
    "CAACAgQAAxkBAALRi2NZXUgjZCT775L5Nr0XrLbQ6XIpAAK_EQACpvFxHq2xh5JRVJNrKgQ",
    "CAACAgQAAxkBAALRjGNZXUs6YPggISBdtg4nXaU0vjNzAALqCwACbCIRU61ZQKi3F88DKgQ",
    "CAACAgQAAxkBAALRjWNZXUvETcfHR2Yi9ftTQLLP2uD8AAIVDAAC1SMQU-QrCHEcbz8rKgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]
