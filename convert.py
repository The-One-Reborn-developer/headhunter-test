import os
import aiohttp

from dotenv import load_dotenv, find_dotenv


async def convert(first_currency, second_currency, amount):
    load_dotenv(find_dotenv())
    
    url = f"https://api.exchangeratesapi.io/v1/latest?access_key={os.getenv("API")}&from={first_currency}&to={second_currency}&amount={amount}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            return data["rates"][second_currency]