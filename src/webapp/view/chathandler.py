#coding=utf8
import uuid
from basehandler import BaseHandler
from basesockethandler import BaseSocketHandler, chatData

class RoomHandler(BaseHandler):
    def get(self):
        self.render("chat.html", messages = chatData.getCache())

    def post(self):
        pass

class ChatSocketHandler(BaseSocketHandler):
    def on_message(self, message):
        chat = {
            "id": str(uuid.uuid4()),
            "body": message,
            "me":1,
            "name":"gm",
            }
        chat["html"] = self.to_basestring(self.render_string("message.html", message=chat))
        chatData.msgtocache(chat)
        