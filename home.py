import webapp2
import render
from models import PostDefault


class landing(webapp2.RequestHandler):
    def get(self):
        v = {'PostDefault': PostDefault}
        html = render.page(self, "templates/landing.html",v)
        self.response.out.write(html)
