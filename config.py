from os import getenv

MONGO_HOST = getenv("MONGO_HOST", "127.0.0.1")
MONGO_PORT = getenv("MONGO_PORT", "27017")
MONGO_DB_NAME = getenv("MONGO_DB_NAME", "visa")
