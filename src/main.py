from fastapi import FastAPI, HTTPException
from module.chat_ai import ChatAI
from model.image_analyzer import ImageAnalyzer

app = FastAPI()

@app.post("/analyze-image")
async def analyze_image_async(data: ImageAnalyzer):
    chat = ChatAI()
    try:
        response = chat.analyze_image(data)
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Request could not be made")