from basehandler import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.get_argument("u")
        password = self.get_argument("p")
        if username == "zhaolu" and password == "123":
            self.set_secure_cookie("user", username)
            print(self.get_secure_cookie("user"))
            self.redirect("/chatroom")
        else:
            self.render("login.html")