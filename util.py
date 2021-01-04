import json
import re
import traceback

import requests
import tushare as ts
from bs4 import BeautifulSoup

ts.pro_api('5b2839d7f9616d9711dc42852a8fa31e02c8ccc4c231e33d72a93242')


def calRealCode(fundCode, start_date=None, end_date=None):
    url = 'http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code={}&topline=20'.format(fundCode)
    print(fundCode)
    r = requests.get(url)
    # print(r.text)
    # print(len(r.text))
    html = re.findall('content:"(.*?)"', r.text)
    # print(html[0])
    soup = BeautifulSoup(html[0], 'html.parser', from_encoding='utf-8')
    # print(soup.find_all("tr"))
    total = 0
    for index, item in enumerate(soup.find_all("tbody")[0].find_all("tr")):
        # print(index,": ",item)
        # print(index,": ",re.findall('quote.eastmoney.com/(.*?).html', item.a['href'])[0])
        # print(item.find_all("td")[6])
        # print(index,": ",item.find_all("td")[6].get_text())
        location = re.findall('quote.eastmoney.com/(.*?).html', item.a['href'])[0][:2]
        if location not in ['sz', 'sh', 'SZ', 'SH']:
            continue
        total += float(item.find_all("td")[6].get_text()[:-1])
    # print(total)
    rate = 0
    for index, item in enumerate(soup.find_all("tbody")[0].find_all("tr")):
        # print(index,": ",item)
        code = re.findall('quote.eastmoney.com/(.*?).html', item.a['href'])[0][2:]
        location = re.findall('quote.eastmoney.com/(.*?).html', item.a['href'])[0][:2]
        if location not in ['sz', 'sh', 'SZ', 'SH']:
            continue
        # print(index,": ",code)
        # print(item.find_all("td")[6])
        weight = float(item.find_all("td")[6].get_text()[:-1])
        # print(index,": ",weight)
        df = ts.pro_bar(ts_code=code + '.' + location.upper(), adj='qfq', start_date=start_date, end_date=end_date)
        # print(code + '.' + location.upper())
        df_list = df['close'].tolist()
        rate += (df_list[0] - df_list[-1]) / df_list[-1] * (weight / total)
    # print(rate)
    return rate


def judgeFund(data: list, span: int):
    data = data[max(len(data) - span, 0):]
    # print(data)
    try:
        pre = json.loads(data[0])
    except Exception as e:
        print(data[0])
    winNum = 0
    diffRate = 0
    start = json.loads(data[0])
    end = json.loads(data[-1])
    rate = (float(end["dwjz"]) - float(start["dwjz"])) / float(start["dwjz"]) * 100
    fundCode = start["fundcode"]
    calNum = 0
    for item in data[1:]:
        cur = json.loads(item)
        if cur["jzrq"] == pre["gztime"].split()[0]:
            calNum += 1
            dailyRate = (float(cur["dwjz"]) - float(pre["dwjz"])) / float(pre["dwjz"])
            diffRate += dailyRate * 100 - float(pre["gszzl"])
            if float(pre["gszzl"]) < dailyRate:
                winNum += 1
        pre = cur
    winPercent = winNum / max(calNum, 0.000001)
    # res={"winPercent":winPercent,"diffRate":diffRate,"rate":rate,"winNum":winNum,"fundcode":pre["fundcode"],"name":pre["name"]}
    # 新增代码计算持仓股票的变化率
    try:
        estimateRate = calRealCode(fundCode=fundCode, start_date=start['jzrq'], end_date=end['jzrq']) * 100
        diffEsRate = rate - estimateRate
    except Exception as e:
        traceback.print_exc()
        diffEsRate = 0
        estimateRate = 0
    res = {"winPercent": "{:^.5f}".format(winPercent), "diffRate": "{:^.5f}".format(diffRate),
           "rate": "{:^.5f}".format(rate), "winNum": "{:^3}".format(winNum), "fundcode": pre["fundcode"],
           "esRate": "{:^.5f}".format(estimateRate), "diffEsRate": "{:^.5f}".format(diffEsRate), "name": pre["name"], }
    print(res)
    return res
