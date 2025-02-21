from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from module.chat_ai import ChatAI

class ImageAnalyzer(BaseModel):
        chat_prompt: str
        base64: str

app = FastAPI()

@app.post("/analyze-image")
async def analyze_image_async(data: ImageAnalyzer):
    chat = ChatAI()
    try:
        response = chat.analyze_image_async(data.chat_prompt, data.base64)
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Request could not be made")