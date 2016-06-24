#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-22 16:54:47
# @Author  : ivon
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from application import application

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print ("Development server is running at http://0.0.0.0:%s" % options.port)
    print ("Quit the server with Control-C")

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
