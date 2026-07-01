import httpx

from app.core.settings import get_settings

settings = get_settings()


class OpenRouterService:

    @staticmethod
    def generate_text(prompt: str) -> str:

        response = httpx.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.openrouter_api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": settings.openrouter_model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                "temperature": 0,
            },
            timeout=60,
        )

        if response.status_code != 200:
            print("STATUS:", response.status_code)
            print("BODY:", response.text)
            return None

        data = response.json()

        return data["choices"][0]["message"]["content"]
