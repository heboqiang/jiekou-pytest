"""
操作mysql的类
"""
import pymysql
# from common.config import myconf

class ReadSQL(object):
    """操作mysql的类"""
    def __init__(self):
        # 连接到数据库，创建游标
        # self.conn = pymysql.connect(host='test.lemonban.com',
        #                        port=3306,
        #                        user='test',
        #                        password='test',
        #                        database='future')
        self.coon = pymysql.connect(
            host='192.168.3.12',            # 数据库地址
            port=3306,         # 端口（配置文件传入的是字符串格式，所以这里取值的时候，用getint的方法 ）
            user='jper',            # 账号
            password='MURL1opdfpIA4y1d',    # 密码
            database='jp_shop',    # 要操作的数据库名
            charset='utf8'       # 指定编码格式
        )
        #创建一个游标
        self.cur = self.coon.cursor()

    def close(self):
        # 关闭游标
        self.cur.close()

        # 断开连接
        self.coon.close()

    def find_one(self, sql):
        """查询一条数据"""
        self.coon.commit()  # 更新数据库到最新状态
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self, sql):
        """返回sql语句查询到的所有结果"""
        self.coon.commit()  # 更新数据库到最新状态
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_count(self, sql):
        """查询数据的条数"""
        self.coon.commit()  # 更新数据库到最新状态
        count = self.cur.execute(sql)
        return count

if __name__ == '__main__':
    sql = "SELECT * FROM jp_user WHERE phone = '18821768014';"
    # sql2 = "SELECT * FROM member LIMIT 5;"

    db = ReadSQL()
    res = db.find_one(sql)
    print(res)

    print('----------------------------------------')
    #
    # res2 = db.find_all(sql2)
    # for i in res2:
    #     print(i)
    #
    # print('----------------------------------------')
    #
    # res3 = db.find_count(sql2)
    # print(res3)