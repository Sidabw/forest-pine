# -*- coding: UTF-8 -*-
import MySQLdb
import sys

# mysql 使用学习

# 解决乱码异常。
reload(sys)
sys.setdefaultencoding("utf-8")

brew = MySQLdb.connect("localhost", "root", "root", "brew", charset='utf8')  # 链接数据库

# select
cursor = brew.cursor()  # 获取游标.执行之后游标会向前移动。
cursor.execute("select * from zk_user ")  # 执行sql
# dataOne = cursor.fetchone() # 获取一条结果
data = cursor.fetchall()  # 获取所有执行结果
print
data[0][6].decode('utf-8')
print
cursor.rowcount

# insert
# sql = "insert into user(id, name) values('3', 'feiyiiii')"
# try:
#     cursor.execute(sql)
#     brew.commit()
# except BaseException, baseException:
#     print baseException
#     brew.rollback()
# finally:
#     brew.close()

# update
# sql = "update user set name = 'feiyiaaa' where id = 3"
# try:
#     cursor.execute(sql)
#     brew.commit()
# except BaseException, baseException:
#     print baseException
#     brew.rollback()
# finally:
#     brew.close()

# delete
# 同上...  sql = "delete from user where id =3"
