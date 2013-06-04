import cgi
import os
import webapp2
import render
from forms import MedBoxForm

class main(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Peace Corps Volunteer',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/siteadmin/home.html",template_values)
        self.response.out.write(html)

class form(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Peace Corps Volunteer',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/siteadmin/medbox_form.html",template_values)
        self.response.out.write(html)

class boxform(webapp2.RequestHandler):
    def get(self, site):
        v = {'MedBoxForm': MedBoxForm()}
        html = render.page(self, "templates/siteadmin/postsupplyform.html",v)
        self.response.out.write(html)
    def post(self, site):
        self.response.out.write("foo")