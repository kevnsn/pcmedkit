from models import *

# from google.appengine.ext import db
# from google.appengine.ext import webapp
# from google.appengine.ext.webapp import template
# from google.appengine.ext.webapp.util import run_wsgi_app


from google.appengine.ext.db import djangoforms


class VolunteerForm(djangoforms.ModelForm):
    class Meta:
        model = Volunteer
        #exclude = ['added_by']

