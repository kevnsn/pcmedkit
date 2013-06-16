import webapp2
import render
from models import PostDefault
from google.appengine.ext import db

class main(webapp2.RequestHandler):
    def get(self):
        v = {}
        v['region_codes'] = {
            'Africa': "AFR",
            'Europe, Mediterranean, and Asia Region': "EMA",
            'Inter-America and Pacific Region': "IAP",
            "Other": "Other",
        }
        v['regions'] = sorted([r for r in v['region_codes']])
        v['PostDefault'] = PostDefault
        html = render.page(self, "templates/superadmin/landing.html",v)
        self.response.out.write(html)


class form(webapp2.RequestHandler):
    def get(self, form_name=""):
        v = {}
        k = self.request.get('k')
        v['post_default'] = db.get(k)
        html = render.page(self, "templates/forms/post_default.html",v)
        self.response.out.write(html)
    def post(self, form_name=""):
        self.response.out.write("foo")
