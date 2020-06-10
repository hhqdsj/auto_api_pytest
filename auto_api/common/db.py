# -*- coding: utf-8 -*-
# @Author: hhqdsj

import pymysql

class DB:

    def __init__(self,host,port,user,passw,database,charset):
        self.host=host
        self.port=port
        self.user=user
        self.passw=passw
        self.database=database
        self.charset=charset

    # 连接database
    def connect(self):
        self.conn=pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.passw,
            database = self.database,
            charset = self.charset
        )
        return self.conn

    # 执行sql，并将运行的结果返回
    def run_sql(self,conn,sql):
        self.cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL语句
        self.cursor.execute(sql)
        self.conn.commit()
        self.data =self.cursor.fetchone()
        self.cursor.close()
        # 返回sql的运行结果
        return self.data


    def close_connect(self,conn):
        # 关闭数据库连接
        conn.close()








