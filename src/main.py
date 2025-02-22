from fastapi import FastAPI, HTTPException
from multiprocessing import freeze_support
from module.chat_ai import ChatAI
from model.image_analyzer import ImageAnalyzer
import uvicorn
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/analyze-image")
async def analyze_image_async(data: ImageAnalyzer):
    try:
        chat = ChatAI()
        response = chat.analyze_image(data)
        return response
    except ValueError as error:
        raise HTTPException(status_code=401, detail=str(error))
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=503, detail="An error has occurred while handling the request.")

if (__name__ == '__main__'):
    freeze_support()
    uvicorn.run(app, host="0.0.0.0", port=8000)