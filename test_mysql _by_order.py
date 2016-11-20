import datetime
import pymysql.cursors
from utils import log, now


# 执行sql语句
def create(cursor):
    sql_create = '''
    CREATE TABLE people (
        id	INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        username	CHAR(20) NOT NULL ,
        password	CHAR(20) NOT NULL,
        email	CHAR(20)
    )
    '''
    # 用 execute 执行一条 sql 语句
    cursor.execute(sql_create)
    print('创建成功')


def insert(cursor, username, password, email):
    sql_insert = '''
    INSERT INTO
        people(username, password, email)
    VALUES
        (%s, %s, %s)
    '''
    # 参数拼接要用 %s，execute 中的参数传递必须是一个 tuple 类型
    cursor.execute(sql_insert, (username, password, email))
    print('插入数据成功')


def select(cursor):
    sql = '''
    SELECT
        *
    FROM
        people
    '''
    cursor.execute(sql)
    # 获取剩余结果的第一行数据
    # result = cursor.fetchone()
    # 获取剩余结果前n行数据
    # result = cursor.fetchmany(3)
    # 获取剩余结果所有数据
    result = cursor.fetchall()
    for row in result:
        print(row)


def delete(cursor, user_id):
    sql_delete = '''
    DELETE FROM
        people
    WHERE
        id=(%s)
    '''
    cursor.execute(sql_delete, (user_id,))
    print('插入数据成功')


def update(cursor, user_id, email):
    sql_update = '''
    UPDATE
        people
    SET
        email=(%s)
    WHERE
        id=(%s)
    '''
    cursor.execute(sql_update, (email, user_id))


def main():
    # 连接配置信息
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'password',
        'db': 'codee',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    # 创建连接
    connection = pymysql.connect(**config)
    print("打开了数据库")
    cursor = connection.cursor()
    # 打开数据库后 就可以用 create 函数创建表
    # create(cursor)
    # 然后可以用 insert 函数插入数据
    # insert(cursor, 'gua', '123', 'guaja')
    # 可以用 delete 函数删除数据
    # delete(cursor, 2)
    # 可以用 update 函数更新数据
    # update(cursor, 1, 'gua@cocode.cc')
    # select 函数查询数据
    select(cursor)
    # 必须用 commit 函数提交你的修改
    # 否则你的修改不会被写入数据库
    connection.commit()
    # 用完数据库要关闭
    connection.close()


if __name__ == '__main__':
    main()
