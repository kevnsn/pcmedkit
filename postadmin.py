import cgi
import os
from datetime import datetime
import webapp2
import render
from forms import VolunteerForm
from models import Volunteer, MedKit, PostDefault, SupplyRequest


class supply_form(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'post_code': post_code}
        html = render.page(self, "templates/postadmin/supply_form.html", v)
        self.response.out.write(html)
    def post(self, post_code):
        v = {'post_code': post_code}
        html = render.page(self, "templates/postadmin/supply_form.html", v)
        self.response.out.write(html)

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
        allrequests = SupplyRequest.all()
        allrequests.order("-date")
        v['allrequests'] = allrequests
        html = render.page(self, "templates/postadmin/requests_table.html", v)
        self.response.out.write(html)

class medkit(webapp2.RequestHandler):
    def get(self, post_code):
        v = {'vf': VolunteerForm(),
             'path': self.request.path,
             'post_code': post_code}
        html = render.page(self, "templates/postadmin/assign_medkit.html",v)
        self.response.out.write(html)
    def post(self, post_code):
        post_def_record = PostDefault.all().filter('slug =', post_code)
        # post_def_record = PostDefault.get_by_key_name(str(post_code))
        # I haven't found an good way to write the key names for dev server bulk loader
        # if you want to recreate production behavior inside dev server run the following commented-out code within the dev server "interactive console"
        # from models import PostDefault
        # for p in PostDefault.all():
        #     p.key_name = p.slug
        #     p.put()
        #     print p.slug + " -- Done!"
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
                    post_default = post_def_record,
                )
                new_v.put()
                new_kit = MedKit(
                    date_issued = datetime.now(),
                    in_use = True,
                    supply_requests = [],
                    post_default = None,
                    volunteer = new_v
                )
                new_kit.put()
                v = {'Volunteer': new_v, 'MedKit': new_kit, 'post_code': post_code}
                html = render.page(self, "templates/postadmin/confirmation.html",v)
                self.response.out.write(html)
            else:
                self.response.out.write("invalid entry for one of the form items")
        else:
            render.not_found(self)