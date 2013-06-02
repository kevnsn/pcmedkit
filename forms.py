from models import *


from google.appengine.ext.db import djangoforms

class VolunteerForm(djangoforms.ModelForm):
    class Meta:
        model = Volunteer
        #exclude = ['added_by']

