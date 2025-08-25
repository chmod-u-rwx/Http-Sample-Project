
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import hashlib

app = FastAPI()


class InputData(BaseModel):
    text: str

@app.post("/process")
async def process(data: InputData):
    await asyncio.sleep(3)
    result = hashlib.sha256(data.text.encode()).hexdigest()

    return {"input": data.text, "result": result}

@app.get("/health")
async def health_check():
    return "healthy"
