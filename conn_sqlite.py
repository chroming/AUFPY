# coding: utf-8

import sqlite3
import time


class ConnSqlite(object):
    """
    sqlite连接类
    """

    def __init__(self):
        self.conn = sqlite3.connect('SECRET.DB')
        self.cursor = self.conn.cursor()

    def create_table(self):
        create_sql = "CREATE TABLE TOTP (ID varchar(20) primary key, " \
                     "NAME varchar(20), SECRETCODE varchar(50), TIME varchar(30))"
        self.cursor.execute(create_sql)

    def insert_value(self, name, secret):
        insert_sql = "INSERT INTO TOTP (NAME, SECRETCODE, TIME) VALUES ('%s', '%s', '%s')" % (name, secret, time.strftime("%Y%m%d%H%M%S", time.localtime()))
        self.cursor.execute(insert_sql)
        self.conn.commit()

    def select_code(self, name):
        select_sql = "SELECT SECRETCODE from TOTP where name='%s'" % name
        self.cursor.execute(select_sql)
        return self.cursor.fetchone()

    def close_conn(self):
        self.conn.close()

