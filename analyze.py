import json
import time
import util
import redis
redis=redis.Redis(host="127.0.0.1",port=6379,db=2,decode_responses=True)
# print(redis.keys())
lis=[]
for key in redis.keys():
    allData=redis.lrange(key,0,-1)
    lis.append(util.judgeFund(allData,30))

print("sort winPercent: **********************************")
lis.sort(key=lambda x:x["winPercent"],reverse=True)
for i in lis[:10]:
    print(i)
print("sort rate: ****************************************")
lis.sort(key=lambda x:x["rate"],reverse=True)
for i in lis[:10]:
    print(i)



