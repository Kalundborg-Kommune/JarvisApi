from pydantic import BaseModel

class ImageAnalyzer(BaseModel):
        chat_prompt: str
        base64: str