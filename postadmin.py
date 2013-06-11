import cgi
import os
from datetime import datetime
import webapp2
import render
from forms import VolunteerForm, SupplyForm
from models import Volunteer, MedKit, PostDefault, SupplyRequest, Supply
import utilities


class landing(webapp2.RequestHandler):
    def get(self, post_code=""):
        v = {'PostDefault': PostDefault}
        html = render.page(self, "templates/postadmin/landing.html", v)
        self.response.out.write(html)


class supply_form(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'sf': SupplyForm(), 'post_code': post_code}
        v['supplies'] = Supply.all().order('name')
        html = render.page(self, "templates/postadmin/supply_form.html", v)
        self.response.out.write(html)
    def post(self, post_code):
        post_def_record = PostDefault.all().filter('slug =', post_code)
        if post_def_record != None:
            f = SupplyForm(self.request.POST)
            if f.validate():
                new_s = Supply(
                    name = f.name.data,
                    description = f.description.data,
                    maximum = f.maximum.data,
                )
                new_s.put()
                pd = post_def_record.get()
                pd.supplies.append(new_s.key())
                pd.put()
                re_url = "/admin/%s/supplies" % (post_code)
                self.redirect(re_url)
            else:
                self.response.out.write("invalid entry click the 'back button'")
                # TODO should redirect to a proper error
        else:
            render.not_found(self)

class requests_table(webapp2.RequestHandler):
    '''
    Present a table to the post administrator with all requests and their status
    '''
    # supplies = db.ListProperty(db.Key)
    # date = db.DateTimeProperty(required=False)
    # quantities = db.ListProperty(int)
    # delivery_event = db.ReferenceProperty(DeliveryEvent)
    # status = db.StringProperty(required=True, choices=set(["Requested", "In Transit", "Completed", "See Notes"]), default="Requested")
    # status_notes = db.TextProperty(required=False)
    # volunteer_notes = db.TextProperty(required=False)

    def get(self, post_code):
        v = {'post_code': post_code}
        q = PostDefault.all().filter("slug =", post_code.lower())
        if q.count() > 0:
            all_requests = SupplyRequest.all().filter("post_default =", q.get())
            v['requests'] = utilities.sr_improver(all_requests)
            html = render.page(self, "templates/postadmin/requests_table.html", v)
            self.response.out.write(html)
        else:
            self.response.out.write("Post not found")


class medkit(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'vf': VolunteerForm(),
             'path': self.request.path,
             'post_code': post_code}
        html = render.page(self, "templates/postadmin/assign_medkit.html",v)
        self.response.out.write(html)
    def post(self, post_code):
        post_def_record = PostDefault.all().filter('slug =', post_code)
        if post_def_record != None:
            f = VolunteerForm(self.request.POST)
            if f.validate():
                new_v = Volunteer(
                    first_name = f.first_name.data,
                    last_name = f.last_name.data,
                    phone = f.phone.data,
                    email = f.email.data,
                    project = f.project.data,
                    sitelocation = f.sitelocation.data,
                    notes = f.notes.data,
                    cos = f.cos.data,
                    trainee_input = "",
                )
                new_v.put()
                new_kit = MedKit(
                    date_issued = datetime.now(),
                    in_use = True,
                    delivery_events = [],
                    volunteer = new_v,
                    post_default = post_def_record.get(),
                )
                new_kit.put()
                v = {'Volunteer': new_v, 'MedKit': new_kit, 'post_code': post_code}
                html = render.page(self, "templates/postadmin/confirmation.html",v)
                self.response.out.write(html)
            else:
                self.response.out.write("invalid entry for one of the form items")
        else:
            render.not_found(self)