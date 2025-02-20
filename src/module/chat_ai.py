import base64
import os
from mistralai import Mistral
from mistralai.models import UserMessage

class ChatAI:
        def __init__(self):
            self.model = "pixtral-12b-2409"
            self.client = Mistral(os.environ.get('MISTRAL_API_KEY', None))

        async def analyze_image_async(self, base64):
            chat_response = await self.client.chat.complete_async(
                model=self.model,
                messages=[
                    UserMessage(
                        content=[
                            {
                                "type": "text",
                                "text": "Udtræk informationer fra denne kvittering"
                            },
                            {
                                "type": "image_url",
                                "image_url": f"data:image/jpeg;base64,{base64}"
                            }
                        ]
                    )
                ]
            )

            return chat_response.choices[0].message.content