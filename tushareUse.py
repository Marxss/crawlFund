import tushare as ts

tokens=['a230cd00b15bc16d9e292212b750841ea6794a8709dc06d0f42309c7',
       '64a5811afb0129855a4e9d38f568ed93916b09b870fe5dcac7cc6a93',
       '33664cc9d24bd1f57f14f7d8c453d8862f97c2fae242c589778a61ad',
       'c47d4477fd5d06fc894700a35e7f1fa99493f1c90d4a251df42a90d5']

for token in tokens:
    ts.pro_api(token)
    print(ts.pro_bar(ts_code='000001.SZ', adj='hfq', start_date='20190101', end_date='20190211'))