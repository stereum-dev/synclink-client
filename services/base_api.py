import httpx
from loguru import logger


class API:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.client = httpx.AsyncClient(base_url=apiUrl)

    async def request(self, url_path):
        try:
            response = await self.client.get(url_path)
            response.raise_for_status()

            return response.json()
        except Exception as exc:
            logger.error(f"ERROR: {exc}")
