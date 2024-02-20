# 非同期処理
import asyncio
import datetime
import httpx as requests


async def main():
    t = datetime.datetime.now()
    urls = [f"https://j-net21.smrj.go.jp/snavi/articles?category%5B0%5D=2&order=DESC&perPage=10&page={i}" for i in range(1, 100)]
    async with requests.AsyncClient() as client:
        tasks = [client.get(u) for u in urls]
        await asyncio.gather(*tasks, return_exceptions=True)
    print(datetime.datetime.now() - t)
    # 1~19ページで1秒くらい。
    # 1~99ページで5秒くらい。

asyncio.run(main())
