# coding: utf-8

import pyotp
import time
import datetime


def get_code(_secret):
    totp = pyotp.TOTP(_secret)
    _now_code = totp.now()
    return _now_code


def get_loop(_secret):
    print get_code(_secret)
    while True:
        residual_time = int(30 - time.mktime(datetime.datetime.now().timetuple()) % 30)
        if residual_time == 30:
            now_code = get_code(_secret)
            print now_code
        time.sleep(1)

if __name__ == '__main__':
    secret = raw_input('input secret code: ')
    get_loop(secret)
