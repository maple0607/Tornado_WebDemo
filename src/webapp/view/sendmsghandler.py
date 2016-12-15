#coding=utf8
from basehandler import BaseHandler
from webapp.service.chatdata import chatData
import os.path
import uuid
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
class SvrMsgHandler(BaseHandler):
    def get(self):
        msg = self.get_argument("msg")
        chat = {
            "id": str(uuid.uuid4()),
            "body": msg,
            "color":"red",
            "name":"gm"
            }
        chat["html"] = tornado.escape.to_basestring(self.render_string("message.html", message=chat))
        chatData.msgtocache(chat)
        self.flush()
        self.finish()