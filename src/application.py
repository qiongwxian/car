#coding:utf-8
import tornado.web
import os
from urls import urls

template_path = os.path.join(os.path.dirname(__file__),"templates")
static_path = os.path.join(os.path.dirname(__file__),"static")

SETTINGS = dict(
template_path = template_path,
static_path = static_path,
)

application = tornado.web.Application(
                handlers = urls,
                **SETTINGS
)
