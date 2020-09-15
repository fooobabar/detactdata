import cx_Oracle
import xlwt
import datetime
'''
工具模块，用来执行SQL与导出xls 文件
'''

class execsql(object):

    def __init__(self,username,password,estns):
        '''
        初始化连接
        :param username: scott
        :param password: tiger
        :param estns: 127.0.0.1:1521/orcl
        '''
        self.conn = cx_Oracle.connect(username, password, estns)

    def is_query_only(self,v_sql) -> bool:
        '''
        判断是否为查询操作
        :param v_sql: SQL文本
        :return: boolean
        '''
        return v_sql.strip().lower().startswith('select')

    def execsql(self,v_sql:str) -> cx_Oracle.Cursor:
        '''
        执行SQL返回查询结果
        :param v_sql: SQL文本
        :return: 查询结果
        '''
        cursor = self.conn.cursor()

        if self.is_query_only(v_sql):
            self.result = cursor.execute(v_sql)
            return True

        return False

    def getResult(self):
        return self.result

    def expxlsx(self,xlsxname:str):
        '''
        导出SQL查询内容到excel，只能导出xls格式，
        第一个sheet是查询结果，第二个sheet是查询SQL
        :param xlsxname: 对xls文件命名
        :param result: SQL查询结果
        :return: None
        '''
        # 获取跑批时间
        cur_time = datetime.datetime.now()
        book = xlwt.Workbook()

        # 创建sheet1 保存数据
        query_result = book.add_sheet('query_result')

        # 写入表头
        for col, field in enumerate([ x[0] for x in self.result.description ]):
            query_result.write(0, col, field)

        # 写入数据
        all_data = self.result.fetchall()
        row = 1
        for data in all_data:
            for col, field in enumerate(data):
                query_result.write(row, col, field)
            row += 1

        # 创建sheet2 保存SQL
        sqlstmt = book.add_sheet('sql_statement')
        sqlstmt.write(0,0,self.result.statement)

        book.save("xls/{}_{}.xls".format(xlsxname,cur_time.strftime("%Y%m%d%H%M%S")))

