import os
import uvicorn
from app import create_app
from fastapi import FastAPI

app: FastAPI = create_app()
# app = FastAPI()

@app.get("/api")
async def api() -> dict:
    return {"message": "Hello, ai_wechat!"}


if __name__ == "__main__":
    uvicorn.run(
        'main:app', 
        host="0.0.0.0", 
        port=8000, 
        reload=True
        )