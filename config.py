from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = 12380656
API_HASH = "d927c13beaaf5110f25c505b7c071273"

BOT_TOKEN = "7944175084:AAFNDr6fIKd4t__0Nj0yrMtrdXe2vY_FrHs"
#OWNER_ID = int(getenv("8060797897"))
OWNER_ID = int(getenv("OWNER_ID", "7224419362"))
MONGO_DB_URI = "mongodb+srv://architect2002:architect2002@cluster0.ccinu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MUST_JOIN = getenv("MUST_JOIN", "The_Architect04")
