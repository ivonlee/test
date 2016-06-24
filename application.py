#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-06-23 9:00:47
# @Author  : ivon
from url import url

import tornado.web
import os

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics"),
    debug = True
    )

application = tornado.web.Application(
    handlers = url,
    **settings
    )
