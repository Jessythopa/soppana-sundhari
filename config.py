from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "6701285365:AAEKn6vbsY6D9uFYqYzoE7BO-Wefj-qjtQM")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://moni:<password>@cluster0.i3djv5s.mongodb.net/?retryWrites=true&w=majority",
)
START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/6e26583b2d4f1eed61ce1.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
