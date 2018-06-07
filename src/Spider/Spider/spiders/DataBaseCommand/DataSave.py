import pymysql
from .ConntionCreate import ConnectionCreate

class DataSave:

    def InserWebData(self,data,url):
        conntionCreate = ConnectionCreate()
        db = conntionCreate.MysqlCreate()
        #创建游标
        cursor = db.cursor()
        # SQL
        sql = r'''INSERT INTO htmldata
               (Data, Url, CreateDate)
               VALUES('2323232', '21212', NOW());'''

        try:
            # 执行SQL语句
            cursor.execute(sql)
            db.commit()
            # 获取所有记录列表
        except Exception as e:
            print(e)
        # 关闭数据库连接
        db.close()


datasave=DataSave()
datasave.InserWebData("dada","dadada")


