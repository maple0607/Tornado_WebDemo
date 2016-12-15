from view import *

default_url = [
	(r"/", LoginHandler),
	(r"/login", LoginHandler),
	(r"/chatroom", RoomHandler),
	(r"/chatsocket", ChatSocketHandler),
	(r"/svrmsg",SvrMsgHandler),
]