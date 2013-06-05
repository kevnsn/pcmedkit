import webapp2
import render


class landing(webapp2.RequestHandler):
    def get(self):
        v = {}
        html = render.page(self, "templates/landing.html",v)
        self.response.out.write(html)

class regions(webapp2.RequestHandler):
    def get(self):
        v = {}
        html = render.page(self, "templates/landing.html",v)
        self.response.out.write(html)
