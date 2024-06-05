from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6701285365:AAEKn6vbsY6D9uFYqYzoE7BO-Wefj-qjtQM")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://moni:<password>@cluster0.i3djv5s.mongodb.net/?retryWrites=true&w=majority",
)
START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/72d486a8eb2e2063e439c.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/72d486a8eb2e2063e439c.jpg"
)
OWNER_ID = int(getenv("OWNER_ID", "6804467181"))
