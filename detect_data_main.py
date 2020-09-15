import re
import opsini
from expxls import execsql
from parsedbinfo import dbInfo

'''
主要逻辑
'''
def main():
    # 获取标签和SQL列表
    strtime = ""
    lst = []
    strtime, lst = opsini.getlst()

    dbinfo = dbInfo()

    #获取互联网测试案例SQL
    v_sql = '''SELECT *
  FROM ECIF_MDM.TEMP_TEST_MDM_CASE_HLW F
 WHERE F.ID NOT IN  ('13','14','21','22','18','17','5','6','25','26','1','2','9','10')
   and f.count_sql != 0 
 order by ID'''

    # 创建query对象
    query=execsql(dbinfo.getUsername('ecif'),dbinfo.getPassword('ecif'),dbinfo.getEstns('ecif'))

    if query.execsql(v_sql):
        result=query.getResult()

        rowdata = result.fetchone()
        while rowdata:
            patt = 'select .+?from'  # 匹配模式
            case_id = rowdata[0]  # 测试案例id

            # 替换count(*) 为 *
            case_sql = re.sub(patt, 'select * from ', rowdata[1], 1, re.IGNORECASE | re.DOTALL)

            if case_id not in lst:
                # 如果case_id 没有在lst列表中，则追加，并且运行SQL
                lst.append(case_id)

                # 更新完成才运行SQL
                if opsini.setlst(strtime, lst):
                    # 运行SQL
                    rst = query.execsql(case_sql)

                    # 获得rst 导出excel
                    query.expxlsx(case_id)

            # 进入下一次循环
            rowdata = result.fetchone()

if __name__=="__main__":
    main()


