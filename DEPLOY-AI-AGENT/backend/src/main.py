import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.db import init_db
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app startup
    init_db()
    yield
    #after app startup

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix = '/api/chats')


@app.get("/")
def read_index():
    return {"hello":"world again!!"}

