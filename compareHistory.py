import tushare as ts
import datetime

# stock = ts.get_today_all()
pro = ts.pro_api('5b2839d7f9616d9711dc42852a8fa31e02c8ccc4c231e33d72a93242')
df=ts.pro_bar(ts_code='00700', adj='qfq', start_date='2019-10-01', end_date='2019-10-11')
df = pro.hk_daily(ts_code='00001.HK', start_date='20190101', end_date='20190904')
print(df)
print(df.columns.tolist())
print(df['close'].tolist())
print(len(df['close'].tolist()))

