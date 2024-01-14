import os
import enum
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Header, HTTPException

load_dotenv(".env")

DEV_X_TOKEN = os.getenv("DEV_X_TOKEN")
DATABSE_URI = os.getenv("DATABASE_URI")

class HTTPExceptionResponses(enum):
    FORBIDEN = {403: {"description": "Operation forbidden"}}
    NOT_FOUND = {404: {"description": "Not found"}}


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != DEV_X_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")