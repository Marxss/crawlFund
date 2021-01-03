import json
import time
import util
import redis
import sys
# print(sys.argv)
redis=redis.Redis(host="127.0.0.1",port=6379,db=2,decode_responses=True)
myFund=['007300','004851','270028','005106','002289']
# print(redis.keys())
lis=[]
for key in redis.keys("0*"): # 0*代表基金号，排除其他
    if key in myFund:
        allData=redis.lrange(key,0,-1)
        lis.append(util.judgeFund(allData,30))
print("my fund: **********************************")
for i in lis:
    print(i)