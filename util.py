import json


def judgeFund(data:list,span:int):
    data=data[min(len(data)-span,0):]
    print(data)
    try:
        pre=json.loads(data[0])
    except Exception as e:
        print(data[0])
    winNum=0
    diffRate=0
    rate=(float(json.loads(data[-1])["dwjz"])-float(json.loads(data[0])["dwjz"]))/float(json.loads(data[0])["dwjz"])*100
    calNum=0
    for item in data[1:]:
        cur=json.loads(item)
        if cur["jzrq"]==pre["gztime"].split()[0]:
            calNum+=1
            dailyRate=(float(cur["dwjz"])-float(pre["dwjz"]))/float(pre["dwjz"])
            diffRate+=dailyRate*100-float(pre["gszzl"])
            if float(pre["gszzl"])<dailyRate:
                winNum+=1
        pre=cur
    winPercent=winNum/max(calNum,0.000001)
    # res={"winPercent":winPercent,"diffRate":diffRate,"rate":rate,"winNum":winNum,"fundcode":pre["fundcode"],"name":pre["name"]}
    res={"winPercent":"{:^.5f}".format(winPercent),"diffRate":"{:^.5f}".format(diffRate),"rate":"{:^.5f}".format(rate),"winNum":"{:^3}".format(winNum),"fundcode":pre["fundcode"],"name":pre["name"]}
    # print(res)
    return res
