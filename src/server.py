#coding:utf-8

import tornado.ioloop
import sys

from conf.main import *
from application import application

if __name__ == "__main__":

    application.listen(PORT)
    print 'Development server is running at http://127.0.0.1:%s/' % PORT
    print 'Quit the server with CONTROL-C'
    tornado.ioloop.IOLoop.instance().start()
