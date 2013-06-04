import cgi
import os
import webapp2
from datetime import datetime
from google.appengine.api import search
from google.appengine.api import users
from models import Volunteer
import render

class main(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Peace Corps Volunteer',
            'verb': 'extremely enjoy',
            'volunteers': Volunteer.all()
        }
        html = render.page(self, "templates/volunteer/home.html",template_values)
        self.response.out.write(html)

class form(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Medical Officer',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/volunteer/supply_form.html",template_values)
        self.response.out.write(html)
