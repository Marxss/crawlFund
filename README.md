# crawlFund
爬取天天基金数据

crawl.py 爬取每日基金数据
retryErrorFundCode.py 重复爬取失败的基金数据

analyze.py 分析基金，进行排序
主要是看估算增长率和实际增长率之间的差距
如果估算增长率<实际增长率之,说明基金经理能力不错

myFund.py 看自己的基金情况

主要依赖Redis作数据库

定时设置：
10 15 * * 1-5 python3 /home/ubuntu/crawlFund/crawl.py > /home/ubuntu/crawlFund/daily.log 2>&1 &
23 16-23/1 * * 1-5 python3 /home/ubuntu/crawlFund/retryErrorFundCode.py >> /home/ubuntu/crawlFund/retry.log 2>>1 &
23 0-8/1 * * 2-6 python3 /home/ubuntu/crawlFund/retryErrorFundCode.py >> /home/ubuntu/crawlFund/retry.log 2>>1 &
