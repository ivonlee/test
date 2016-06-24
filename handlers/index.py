#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-23 8:54:47
# @Author  : ivon

import tornado.web
import models.db as mrd

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        user_infos = mrd.main()
        print(user_infos)
        #self.render("index.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.write("welcome you: " + username)
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no thi user.")
