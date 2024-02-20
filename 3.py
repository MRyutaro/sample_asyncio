# 同期処理
import datetime
import requests


def main():
    t = datetime.datetime.now()
    urls = [f"https://j-net21.smrj.go.jp/snavi/articles?category%5B0%5D=2&order=DESC&perPage=10&page={i}" for i in range(1, 100)]
    for url in urls:
        requests.get(url)
    print(datetime.datetime.now() - t)
    # 1~19ページで平均2.4秒
    # 1~99ページで平均26秒


main()
