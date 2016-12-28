# coding:utf-8

import sqlite3
import time


class ConnSqlite(object):

    def __init__(self):
        self.conn = sqlite3.connect('SECRET.DB')
        self.cursor = self.conn.cursor()

    def create_table(self):
        create_sql = "CREATE TABLE TOTP (ID varchar(20) primary key, " \
                     "NAME varchar(20), SECRETCODE varchar(50), TIME varchar(30))"
        self.cursor.execute(create_sql)

    def insert_value(self, name, secret_code):
        insert_sql = "INSERT INTO TOTP (NAME, SECRETCODE, TIME) VALUES ('%s', '%s', '%s')" % (name, secret_code, time.strftime("%Y%m%d%H%M%S", time.localtime()))
        print insert_sql
        self.cursor.execute(insert_sql)
        self.conn.commit()

    def select_code(self, name):
        select_sql = "SELECT secret_code from TOTP where name=%s" % name
        print select_sql
        self.cursor.execute(select_sql)

    def close_conn(self):
        self.conn.close()

