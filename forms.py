from wtforms import Form
from wtforms.ext.appengine.db import model_form
from models import *

from wtforms import BooleanField, TextField, validators, DateTimeField

MedBox_meta = model_form(MedBox, base_class=Form)
Volunteer_meta = model_form(Volunteer, base_class=Form)

class VolunteerForm(Volunteer_meta):
    cos = DateTimeField('COS', format='%m/%d/%Y')
