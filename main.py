from config import MONGO_HOST, MONGO_PORT, MONGO_DB_NAME
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect
from fastapi import FastAPI
from api import user, form
import uvicorn

app = FastAPI()


@app.get("/health")
async def health_check():
    return "OK"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user, prefix="/user")
app.include_router(form, prefix="/form")


def main():
    connect(host=f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB_NAME}")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        log_level="info"
    )


if __name__ == "__main__":
    main()
