import json
import time
import util
import redis
import sys
# print(sys.argv)
redis=redis.Redis(host="127.0.0.1",port=6379,db=2,decode_responses=True)
limitDay=30 #只看最近30天的情况
# print(redis.keys())
lis=[]
for key in redis.keys("0*"): # 0*代表基金号，排除其他
    try:
        allData=redis.lrange(key,0,-1)
    except Exception as e:
        print(key)
        print(str(e))
    lis.append(util.judgeFund(allData,limitDay))


print("sort rate: ****************************************")
lis.sort(key=lambda x:float(x["rate"]),reverse=True)
for i in lis[:int(sys.argv[1])]:
    print(i)
print("sort diffRate: **********************************")
lis.sort(key=lambda x:float(x["diffRate"]),reverse=True)
for i in lis[:int(sys.argv[1])]:
    print(i)
print("sort winPercent: **********************************")
lis.sort(key=lambda x:float(x["winPercent"]),reverse=True)
queryNum=int(sys.argv[1])
num=0
for i in lis:
    if int(i["winNum"])<5:
        continue
    print(i)
    num+=1
    if num>=queryNum:
        break
print("{} days avarge: **********************************".format(limitDay))
allWinPercent=0
allDiffRate=0
allRate=0
for i in lis:
    allWinPercent+=float(i['winPercent'])
    allDiffRate+=float(i['diffRate'])
    allRate+=float(i["rate"])
print("winPercent: {:^.5f}   diffRate: {:^.5f}   rate: {:^.5f}".format(allWinPercent/len(lis),allDiffRate/len(lis),allRate/len(lis)))




