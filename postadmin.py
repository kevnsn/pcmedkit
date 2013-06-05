import cgi
import os
from datetime import datetime
import webapp2
import render
from forms import VolunteerForm
from models import Volunteer, MedBox

class landing(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'post_code': post_code}
        html = render.page(self, "templates/postadmin/landing.html", v)
        self.response.out.write(html)

class supply_form(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'post_code': post_code}
        html = render.page(self, "templates/postadmin/supply_form.html", v)
        self.response.out.write(html)

class requests_table(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'post_code': post_code}
        html = render.page(self, "templates/postadmin/requests_table.html", v)
        self.response.out.write(html)

class medkit(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'vf': VolunteerForm(), 'path': self.request.path}
        html = render.page(self, "templates/postadmin/assign_medkit.html",v)
        self.response.out.write(html)
    def post(self, post_code):
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
        html = render.page(self, "templates/postadmin/confirmation.html",v)
        self.response.out.write(html)