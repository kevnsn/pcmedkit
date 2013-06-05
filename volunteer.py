import webapp2
import render

class landing(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'post_code': post_code}
        html = render.page(self, "templates/volunteer/landing.html", v)
        self.response.out.write(html)
    def post(self, post_code):
        redirect_url = '/post/%s/check_status' % (post_code)
        self.redirect(redirect_url)

class status(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'post_code': post_code}
        html = render.page(self, "templates/volunteer/status_table.html", v)
        self.response.out.write(html)

class request_form(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'post_code': post_code}
        html = render.page(self, "templates/volunteer/request_form.html", v)
        self.response.out.write(html)
    def post(self, post_code):
        redirect_url = '/post/%s/check_status' % (post_code)
        self.redirect(redirect_url)
