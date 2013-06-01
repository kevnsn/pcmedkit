import cgi
import os
import webapp2
from datetime import datetime
from google.appengine.api import search
from google.appengine.api import users
import models
import render

import jinja2

class home(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'name': 'SomeGuy',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/volunteer_home.html",template_values)
        self.response.out.write(html)		
        
app = webapp2.WSGIApplication([('/', home),])
