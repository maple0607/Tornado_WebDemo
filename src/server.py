import os
import sys
from tornado.web import Application
from tornado.options import define, options, parse_command_line
from tornado.ioloop import IOLoop
from webapp import *
import logging
reload(sys)
sys.setdefaultencoding('utf-8')
define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")

class ServerApplication(Application):
    def __init__(self):
        parse_command_line()
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "../res/templates"),
            static_path = os.path.join(os.path.dirname(__file__), "../res/static"),
            debug = options.debug,
            cookie_secret = "N141c78MRsKESllCkcXADffqR5vSZEk7rRU5EUv78LQ=",
            xsrf_cookies = False,
            login_url = "/login",
        )
        super(ServerApplication, self).__init__(default_url, **settings)
    def startup(self):
        options.port if len(sys.argv) != 2 else sys.argv[1]     
        self.listen(options.port)
        print("*****************************************************\n"
              "****************** SERVER STARTUP OK ****************\n"
              "****** Server start on [http://0.0.0.0:8888] ********\n"
              "*****************************************************")
        IOLoop.instance().start()
if __name__ == "__main__":
    ServerApplication().startup()
    
