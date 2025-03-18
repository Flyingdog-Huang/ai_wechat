from fastapi import APIRouter, HTTPException
from app.utils.logs import get_logger
import os

app = APIRouter()
# app = FastAPI()

@app.get("/api")
async def api() -> dict:
    return {"message": "Hello, ai_wechat!"}

@app.get("/exception")
async def exception(name: str) -> dict:
    try:
        print(username)
    except Exception as e:
        logger =  get_logger(os.environ.get("APP_NAME"))
        logger.error(f"发生异常： {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
    # raise ValueError("Test exception")
    return {}