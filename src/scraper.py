from bs4 import BeautifulSoup as bsoup
import asyncio
import httpx

async def async_req(url):
    tries = 0
    while tries < 5:
        try:
            print(f"Extracting {url}")
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                return response
        except KeyboardInterrupt:
            raise KeyboardInterrupt("Abortando...")
        except:
            tries += 1
            await asyncio.sleep(3)

async def async_scrape(url_to_extract):
    page_html = await async_req(url_to_extract)
    soup = bsoup(page_html.content if page_html else '', 
                 features="html.parser")
    return soup

async def main(urls):

    return await asyncio.gather(*[get_dataavail_text(url) for url in urls])

