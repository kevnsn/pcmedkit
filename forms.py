from models import *
from django.conf import settings
settings.configure()

from google.appengine.ext.db import djangoforms

class VolunteerForm(djangoforms.ModelForm):
    class Meta:
        model = Volunteer
        #exclude = ['added_by']

