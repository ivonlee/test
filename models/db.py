#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-23 8:54:47
# @Author  : ivon
from __future__ import print_function

from tornado import ioloop, gen
import tornado_mysql
@gen.coroutine
def main():
    conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='111111', db='autoops')
    cur = conn.cursor()
    sql = "SELECT * FROM users"
    yield cur.execute(sql)
    for row in cur:
        print(row)
    cur.close()
    conn.close()

ioloop.IOLoop.current().run_sync(main)
