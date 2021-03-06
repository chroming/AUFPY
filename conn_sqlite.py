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
        create_sql = "CREATE TABLE TOTP (ID INTEGER PRIMARY KEY AUTOINCREMENT, " \
                     "NAME varchar(20) NOT NULL, SECRETCODE varchar(50) NOT NULL UNIQUE, TIME varchar(30))"
        self.cursor.execute(create_sql)

    def insert_value(self, name, secret):
        insert_sql = "INSERT INTO TOTP (NAME, SECRETCODE, TIME) VALUES ('%s', '%s', '%s')" % (name, secret, time.strftime("%Y%m%d%H%M%S", time.localtime()))
        self.cursor.execute(insert_sql)
        self.conn.commit()

    def select_code(self, name):
        select_sql = "SELECT SECRETCODE FROM TOTP where name='%s'" % name
        self.cursor.execute(select_sql)
        return self.cursor.fetchone()

    def select_all(self):
        select_sql = "SELECT NAME FROM TOTP"
        self.cursor.execute(select_sql)
        return self.cursor.fetchall()

    def close_conn(self):
        self.conn.close()

if __name__ == '__main__':
    conn = ConnSqlite()
    conn.create_table()

