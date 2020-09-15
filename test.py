from parsedbinfo import dbInfo
from expxls import execsql

dbinfo = dbInfo()

print(dbinfo)

print(dbinfo.listDbname())

print(dbinfo.getUsername('dss'))
print(dbinfo.getPassword('dss'))
print(dbinfo.getEstns('dss'))

query=execsql(dbinfo.getUsername('ecif'),dbinfo.getPassword('ecif'),dbinfo.getEstns('ecif'))

query.execsql("select to_char(sysdate,'yyyy-mm-dd') as dt from dual ")

query.expxlsx('dt')

