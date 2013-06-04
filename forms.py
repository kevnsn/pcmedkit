from wtforms import Form
from wtforms.ext.appengine.db import model_form
from models import *

VolunteerForm = model_form(Volunteer, base_class=Form)
MedBoxForm = model_form(MedBox, base_class=Form)
