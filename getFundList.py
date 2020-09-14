import requests
import json
import redis

url="http://fund.eastmoney.com/js/fundcode_search.js"

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.81 Safari/9537.53'}
    data = requests.get(url, headers=headers).content.decode("utf-8")
    return data

if __name__=="__main__":
    content=download_page(url)
    print(content.split('=',1))
    data=content.split('=',1)[-1][:-1]
    print(data)

    redis = redis.Redis(host='127.0.0.1', port=6379)
    redis.set("findList",data)
