#coding=utf8
import tornado
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
from webapp.service.cachedata import CacheData
chatData = CacheData(100)
class BaseSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        chatData.addWriter(self)
    def on_close(self):
        chatData.removeWriter(self)

    def to_basestring(self, msgstr):
        return tornado.escape.to_basestring(msgstr)
