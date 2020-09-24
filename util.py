import json


def judgeFund(data:list,span:int):
    data=data[min(len(data)-span,0):]
    try:
        pre=json.loads(data[0])
    except Exception as e:
        print(data[0])
    winNum=0
    rate=0
    calNum=0.00001
    for item in data[1:]:
        cur=json.loads(item)
        if cur["jzrq"]==pre["gztime"].split()[0]:
            calNum+=1
            dailyRate=(float(cur["dwjz"])-float(pre["dwjz"]))/float(pre["dwjz"])
            rate+=dailyRate
            if float(pre["gszzl"])>dailyRate:
                winNum+=1
        pre=cur
    winPercent=winNum/calNum
    res={"winPercent":winPercent,"rate":rate,"winNum":winNum,"fundcode":pre["fundcode"],"name":pre["name"]}
    print(res)
    return res

        