import httpx
from fastapi import HTTPException
from app.config import settings


class FireworksClient:

    def __init__(self):
        self.base_url = settings.FIREWORKS_BASE_URL.rstrip("/")
        self.api_key = settings.FIREWORKS_API_KEY

    def generate(self, model: str, prompt: str):

        url = f"{self.base_url}/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2,
            "max_tokens": 512,
        }

        try:

            response = httpx.post(
                url,
                headers=headers,
                json=payload,
                timeout=60,
            )

            response.raise_for_status()

            return response.json()

        except httpx.HTTPStatusError as e:

            raise HTTPException(
                status_code=e.response.status_code,
                detail=e.response.json(),
            )

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=str(e),
            )