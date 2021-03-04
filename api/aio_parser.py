import aiohttp
import asyncio
import datetime
from .bs_parser import pa

class Parser:
    async def _call_api(self, address, url, method='get', _json=None, api_url=True, is_photo=False):

        # host = (API_HOST if not api_url else API_HOST + '/api') + address
        # headers = {'Content-Type': 'application/json', 'Host': 'null'}
        async with aiohttp.ClientSession() as session:
            if method == 'get':
                resp = await session.get(address)
            if resp.status != 204:
                a = await resp.text()
                t = pa.get_list_el(a)
                for i in t:
                    try:
                        pa.get_news(i, url)
                    except Exception as e:
                        continue

                return t

    async def get_rate(self, url):
        str_date = datetime.date.today().strftime("%Y/%m/%d")
        html_text = await self._call_api(url + f'/{str_date}', url)

        return 1

    async def raise_error_time(self):
        await asyncio.sleep(10)
        raise Exception('Time!!!!!!!!!!111')

    def pars(self):
        loop = asyncio.get_event_loop()
        # asyncio.gather()
        tasks = [loop.create_task(self.get_rate('https://people.onliner.by')), loop.create_task(self.raise_error_time())]
        wait_tasks = asyncio.wait(tasks)
        loop.run_until_complete(wait_tasks)


parser = Parser()