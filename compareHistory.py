import tushare as ts
import datetime

# stock = ts.get_today_all()
pro = ts.pro_api('5b2839d7f9616d9711dc42852a8fa31e02c8ccc4c231e33d72a93242')
df=ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='2018-01-01', end_date='2018-10-11')
print(df)
print(df.columns.tolist())
print(df['close'].tolist())
print(len(df['close'].tolist()))

import json
import time
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
    print(allData)
    break
