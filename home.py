import cgi
import webapp2
from datetime import datetime
from google.appengine.api import search
from google.appengine.api import users
import models

import jinja2

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
    
class home(webapp2.RequestHandler):
    def get(self):
        message = "hello world"
        self.response.out.write(message)

app = webapp2.WSGIApplication([('/', MainPage),
              ])