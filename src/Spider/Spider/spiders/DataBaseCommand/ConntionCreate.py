import pymysql

    class ConnectionCreate:
        def MysqlCreate(connStr):
            # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
            db = pymysql.connect("localhost", "root", "123456789", "twadspiderdata")
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()

            # 使用 execute()  方法执行 SQL 查询
            cursor.execute("SELECT VERSION()")
            # 使用 fetchone() 方法获取单条数据.
            data = cursor.fetchone()
            print("Database version : %s " % data)

            # 关闭数据库连接
            db.close()