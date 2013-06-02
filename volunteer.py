import cgi
import os
import webapp2
from datetime import datetime
from google.appengine.api import search
from google.appengine.api import users
import models
import render

import jinja2
import forms



class main(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Peace Corps Volunteer',
            'verb': 'extremely enjoy',
            'formhtml': forms.VolunteerForm().as_table()
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
