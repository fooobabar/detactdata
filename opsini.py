import json
import datetime
from typing import List

'''
主要逻辑2
对于相同日期，且已经运行的脚本，做记录，下次不运行。
'''

def getlst() -> (str,List):
    cur_time=datetime.datetime.now()
    strtime = cur_time.strftime("%Y-%m-%d")

    fd=open("detact.ini","r")
    tmp=fd.read()
    fd.close()

    d=json.loads(tmp)
    return strtime,d.get(strtime,[])

def setlst(strtime:str,lst:List) -> bool:
    d={strtime:lst}
    tmp=json.dumps(d)
    fd=open("detact.ini","w")
    if fd.write(tmp):
        return True
    else:
        return False