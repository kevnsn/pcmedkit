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
        message = "hello world"
        #self.response.out.write(message)
        template_values = {
            'name': 'SomeGuy',
            'verb': 'extremely enjoy'
        }
        self.response.out.write(render.page(self, "/templates/base.html",template_values))		
app = webapp2.WSGIApplication([('/', home),])
