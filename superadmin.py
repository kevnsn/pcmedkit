import webapp2
import render
from models import PostDefault

class main(webapp2.RequestHandler):
    def get(self):
        v = {}
        v['region_codes'] = {
            'Africa': "AFR",
            'Europe, Mediterranean, and Asia Region': "EMA",
            'Inter-America and Pacific Region': "IAP",
            "Other": "Other",
        }
        v['PostDefault'] = PostDefault
        html = render.page(self, "templates/superadmin/landing.html",v)
        self.response.out.write(html)
