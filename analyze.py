import json
import time
import util
import redis
import sys
print(sys.argv)
redis=redis.Redis(host="127.0.0.1",port=6379,db=2,decode_responses=True)
# print(redis.keys())
lis=[]
for key in redis.keys("0*"): # 0*代表基金号，排除其他
    try:
        allData=redis.lrange(key,0,-1)
    except Exception as e:
        print(key)
        print(str(e))
    lis.append(util.judgeFund(allData,30))


print("sort rate: ****************************************")
lis.sort(key=lambda x:x["rate"],reverse=True)
for i in lis[:int(sys.argv[1])]:
    print(i)
print("sort winPercent: **********************************")
lis.sort(key=lambda x:x["winPercent"],reverse=True)
queryNum=int(sys.argv[1])
num=0
for i in lis:
    if i["winNum"]<5:
        continue
    print(i)
    num+=1
    if num>=queryNum:
        break



