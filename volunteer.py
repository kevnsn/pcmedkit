import webapp2
import render
from models import MedKit
from google.appengine.ext import db

class landing(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'post_code': post_code}
        html = render.page(self, "templates/volunteer/landing.html", v)
        self.response.out.write(html)
    def post(self, post_code):
        mk_code = self.request.POST['code']
        medkit = MedKit.all().filter('code =', mk_code).get()
        if medkit != None:
            mk = str(medkit.key())
            re_url = "/post/%s/check_status?k=%s" % (post_code, mk)
            self.redirect(re_url)
        else:
            self.response.out.write("Not Found.  Maybe you typed the MedKit code in wrong?")

class status(webapp2.RequestHandler):
    def get(self, post_code):
        mk = self.request.get('k')
        medkit = db.get(mk)
        if medkit != None:
            volunteer = medkit.volunteer
            v = {'post_code': post_code, 'volunteer': volunteer, 'MedKit': medkit, 'mk': mk}
            html = render.page(self, "templates/volunteer/status_table.html", v)
            self.response.out.write(html)
        else:
            render.not_found(self)

class request_form(webapp2.RequestHandler):
    def get(self, post_code):
        mk = self.request.get('k')
        v = {'post_code': post_code, 'mk': mk}
        html = render.page(self, "templates/volunteer/request_form.html", v)
        self.response.out.write(html)
    def post(self, post_code):
        # redirect_url = '/post/%s/check_status' % (post_code)
        self.response.write.out('havent worked this out yet')
