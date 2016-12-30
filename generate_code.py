# coding: utf-8

import pyotp
import time
import datetime
from conn_sqlite import ConnSqlite


def get_code(_secret):
    """
    获取现在的TOTP码
    :param _secret: 安全码
    :return: TOTP码
    """
    totp = pyotp.TOTP(_secret)
    _now_code = totp.now()
    return _now_code


def get_loop(_secret):
    """
    循环获取现在的TOTP码
    :param _secret:安全码
    :return:TOTP码
    """
    print get_code(_secret)
    while True:
        residual_time = int(30 - time.mktime(datetime.datetime.now().timetuple()) % 30)
        if residual_time == 30:
            now_code = get_code(_secret)
            print now_code
        time.sleep(1)


def save_secret():
    """
    name和secret code存入sqlite
    :return: None
    """
    _name = raw_input('Please input name: ')
    _secret = raw_input('Please input secret code: ')
    conn = ConnSqlite()
    conn.insert_value(_name, _secret)
    conn.close_conn()


def get_secret():
    """
    根据name获取TOTP码
    :return:
    """
    _name = raw_input('Please input name: ')
    conn = ConnSqlite()
    _secret = conn.select_code(_name)
    conn.close_conn()
    get_loop(_secret)


if __name__ == '__main__':
    secret = raw_input('input secret code: ')
    get_loop(secret)
