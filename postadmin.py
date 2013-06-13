from datetime import datetime
import webapp2
from google.appengine.ext import db

import render
from forms import VolunteerForm, SupplyForm, DeliveryEventForm
from models import Volunteer, MedKit, PostDefault, SupplyRequest, Supply, DeliveryEvent
import utilities

def simple_validate(v):
    q = PostDefault.all().filter("slug =", v.get('post_code', "").lower())
    if q.count() > 0 and v.get('post_code', "") != "":
        v['post_default'] = q.get()
        v['valid'] = True
    else:
        v['valid'] = False
    return v

class landing(webapp2.RequestHandler):
    def get(self, post_code=""):
        v = {'PostDefault': PostDefault}
        html = render.page(self, "templates/postadmin/landing.html", v)
        self.response.out.write(html)


class supply_form(webapp2.RequestHandler):
    def get(self, post_code):
        v = simple_validate({'post_code': post_code})
        if v['valid']:
            v['sf'] = SupplyForm()
            v['supplies'] = Supply.all().order('name')
            html = render.page(self, "templates/postadmin/supply_form.html", v)
            self.response.out.write(html)
    def post(self, post_code):
        v = simple_validate({'post_code': post_code})
        if v['valid']:
            f = SupplyForm(self.request.POST)
            if f.validate():
                new_s = Supply(
                    name = f.name.data,
                    description = f.description.data,
                    maximum = f.maximum.data,
                )
                new_s.put()
                v['post_default'].supplies.append(new_s.key())
                v['post_default'].put()
                re_url = "/admin/%s/supplies" % (post_code)
                self.redirect(re_url)
            else:
                self.response.out.write("invalid entry click the 'back button'")
                # TODO should redirect to a proper error
        else:
            render.not_found(self)

class requests_table(webapp2.RequestHandler):
    def get(self, post_code):
        v = simple_validate({'post_code': post_code})
        if v['valid']:
            all_requests = SupplyRequest.all().filter("post_default =", v["post_default"])
            v['requests'] = utilities.sr_improver(all_requests)
            html = render.page(self, "templates/postadmin/requests_table.html", v)
            self.response.out.write(html)
        else:
            self.response.out.write("Post not found")


class update(webapp2.RequestHandler):
    def get(self, post_code):
        v = simple_validate({'post_code': post_code})
        if v['valid']:
            sr = db.get(self.request.get("k"))
            v["supply_request"] = utilities.sr_improver([sr])[0]
            v['status_choices'] = list(SupplyRequest.status.choices)
            v["def"] = DeliveryEventForm()
            v["delivery_events"] = DeliveryEvent.all()
            html = render.page(self, "templates/forms/update_supply_request.html", v)
            self.response.out.write(html)
        else:
            self.response.out.write("Post not found")
    def post(self, post_code):
        v = simple_validate({'post_code': post_code})
        if v['valid']:
            PR = self.request.POST
            supply_request = db.get(PR['k'])
            supply_request.status = PR['status']
            supply_request.status_notes = PR['status_notes']
            if PR['delivery_event'] == "Other":
                de = DeliveryEvent(
                    name=PR['name'],
                    date=datetime.strptime(PR['date'], "%m/%d/%Y"),
                    notes=PR['notes']
                )
                de.put()
                PD = v['post_default']
                PD.delivery_events.append(de.key())
                PD.put()
                MK = supply_request.medkit
                MK.delivery_events.append(de.key())
                MK.put()
            else:
                de = db.get(PR['delivery_event'])
            supply_request.delivery_event = de
            supply_request.put()
            redirect = "/admin/" + post_code
            self.redirect(redirect)
        else:
            self.response.out.write("Post not found")




class medkit(webapp2.RequestHandler):
    def get(self, post_code):
        v = simple_validate({'post_code': post_code})
        if v['valid']:
            v['vf'] = VolunteerForm()
        html = render.page(self, "templates/forms/assign_medkit.html",v)
        self.response.out.write(html)
    def post(self, post_code):
        v = simple_validate({'post_code': post_code})
        if v['valid']:
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
                    post_default = v["post_default"],
                )
                new_kit.put()
                v['Volunteer'] = new_v
                v['MedKit'] = new_kit
                html = render.page(self, "templates/postadmin/confirmation.html",v)
                self.response.out.write(html)
            else:
                self.response.out.write("invalid entry for one of the form items")
        else:
            render.not_found(self)