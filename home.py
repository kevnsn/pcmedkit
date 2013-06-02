import cgi
import os
import webapp2
from datetime import datetime
from google.appengine.api import search
from google.appengine.api import users
import models
import render

import jinja2


class vol(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Peace Corps Volunteer',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/volunteer_home.html",template_values)
        self.response.out.write(html)

class sec(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Medical Officer',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/sec_home.html",template_values)
        self.response.out.write(html)
