from fastapi import APIRouter

app = APIRouter()

@app.get("/login")
async def login() -> dict:
    return {"message": "login"}