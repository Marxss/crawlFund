import requests
import json
import re
import time
import random
import redis
redis=redis.Redis(host="127.0.0.1",port=6379,db=2)
url="http://fundgz.1234567.com.cn/js/{}.js?rt=1589463125600"
r = requests.get('http://fund.eastmoney.com/js/fundcode_search.js')
print(r)
cont = re.findall('var r = (.*])', r.text)[0]  # 提取list
ls = json.loads(cont)  # 将字符串个事的list转化为list格式
print(ls)
daihao=[i[0] for i in ls]
for i in daihao:
    try:
        r=requests.get(url.format(i),timeout=3)
        text = re.findall('\((.*?)\)', r.text)[0]
        dic=json.loads(text)
        print(text)
    except Exception as e:
        print("wrong daihao: ",i)
        continue
    latest=redis.lindex(i,-1)
    if latest==None:
        redis.rpush(i,text)
        print("add: ",i)
    else:
        latest=json.loads(latest)
        if latest["gztime"]!=dic["gztime"]:
            redis.rpush(i,text)
            print("add: ", i)
    time.sleep(random.random())
