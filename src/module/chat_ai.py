import base64
import os
from dotenv import load_dotenv
from mistralai import Mistral

class ChatAI:
        def __init__(self):
            load_dotenv()
            self.model = "pixtral-12b-2409"

            if ('MISTRAL_API_KEY' not in os.environ):
                raise Exception("Missing API key")

            self.client = Mistral(os.environ.get("MISTRAL_API_KEY"))

        def analyze_image_async(self, prompt, base64):
            chat_response = self.client.chat.complete(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"{prompt}"
                            },
                            {
                                "type": "image_url",
                                "image_url": f"data:image/jpeg;base64,{base64}"
                            }
                        ]
                    }
                ]
            )

            return chat_response.choices[0].message.content