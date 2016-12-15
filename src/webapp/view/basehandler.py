from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
	def get_curuser(self):
		pass
