import cgi
import os
from datetime import datetime
import webapp2
import render
from forms import VolunteerForm
from models import Volunteer, MedBox

class main(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Peace Corps Volunteer',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/siteadmin/home.html",template_values)
        self.response.out.write(html)

class form(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Peace Corps Volunteer',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/siteadmin/medbox_form.html",template_values)
        self.response.out.write(html)

class boxform(webapp2.RequestHandler):
    def get(self, site):
        v = {'vf': VolunteerForm(), 'path': self.request.path}
        html = render.page(self, "templates/siteadmin/postsupplyform.html",v)
        self.response.out.write(html)
    def post(self, site):
        f = VolunteerForm(self.request.POST)
        new_v = Volunteer(
            first_name = f.first_name.data,
            last_name = f.last_name.data,
            phone = f.phone.data,
            project = f.project.data,
            sitelocation = f.sitelocation.data,
            notes = f.notes.data,
            cos = f.cos.data,
            trainee_input = "foo",
        )
        new_v.put()
        new_box = MedBox(
            date_issued = datetime.now(),
            in_use = True,
            supply_requests = [],
            post_default = None,
            volunteers = [new_v.key()]
        )
        new_box.put()
        v = {'Volunteer': new_v, 'MedBox': new_box}
        html = render.page(self, "templates/siteadmin/confirmation.html",v)
        self.response.out.write(html)