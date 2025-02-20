from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from module.chat_ai import ChatAI

class ImageData(BaseModel):
        base64: str

app = FastAPI()

@app.post("/analyze-image")
async def analyze_image_async(data: ImageData):
    chat = ChatAI()
    try:
        response = await chat.analyze_image_async(data.base64)
        return response
    except:
        raise HTTPException(status_code=404, detail="Request could not be made")