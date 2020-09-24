import requests
import json
import re
import time
import datetime
import random
import redis
redis=redis.Redis(host="127.0.0.1",port=6379,db=2,decode_responses=True)
url="http://fundgz.1234567.com.cn/js/{}.js?rt=1589463125600"
daihao=redis.lrange("errorFundCode",0,-1)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
print("number of errorFundCode: ",len(daihao))
num=0
redis.delete("errorFundCode")
for i in daihao:
    try:
        r=requests.get(url.format(i),timeout=3)
        # print(url.format(i))
        text = re.findall('\((.*?)\)', r.text)[0]
        dic=json.loads(text)
        print("[{}] ".format(num),text)
    except Exception as e:
        print("wrong daihao: ",i)
        redis.lpush("errorFundCode",i)
        continue
    latest=redis.lindex(i,-1)
    if latest==None:
        redis.rpush(i,text)
        num+=1
        print("[{}] new add: ".format(num),i)
    else:
        latest=json.loads(latest)
        if latest["gztime"]!=dic["gztime"]:
            redis.rpush(i,text)
            num += 1
            print("[{}] add: ".format(num), i)
    time.sleep(random.random())
