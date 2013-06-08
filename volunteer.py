import webapp2
import render
from models import MedKit, PostDefault, Supply, DeliveryEvent
from forms import SupplyRequestForm
from google.appengine.ext import db

def simple_validate(v):
    medkit = db.get(v['mk'])
    if medkit == None:
        v['valid'] = False
    else:
        mk_post_code =  medkit.post_default.slug.lower()
        if v['kit_id'] != str(medkit.key().id()):
            v['valid'] = False
        elif mk_post_code != v['post_code'].lower():
            v['valid'] = False
        else:
            v['MedKit'] = db.get(v['mk'])
            v['volunteer'] = v['MedKit'].volunteer
            v['valid'] = True
    return v

class landing(webapp2.RequestHandler):
    def get(self):
        v = {'PostDefault': PostDefault}
        html = render.page(self, "templates/volunteer/landing.html", v)
        self.response.out.write(html)
    def post(self):
        mk_code = self.request.POST['code']
        post_code = self.request.POST['post_code']
        medkit = MedKit.all().filter('code =', mk_code).get()
        if medkit != None:
            m_k = str(medkit.key())
            m_id = str(medkit.key().id())
            re_url = "/%s/%s/check_status?k=%s" % (post_code, m_id, m_k)
            self.redirect(re_url)
        else:
            self.response.out.write("Not Found.  Maybe you typed the MedKit code in wrong?")

class status(webapp2.RequestHandler):
    def get(self, post_code, kit_id):
        v = {}
        v['post_code'] = post_code
        v['kit_id'] = kit_id
        v['mk'] = self.request.get('k')
        v = simple_validate(v)
        if v['valid']:
            v['nav'] = 'status'
            html = render.page(self, "templates/volunteer/status_table.html", v)
            self.response.out.write(html)
        else:
            render.not_found(self)

class request_form(webapp2.RequestHandler):
    def get(self, post_code, kit_id):
        v = {}
        v['post_code'] = post_code
        v['kit_id'] = kit_id
        v['mk'] = self.request.get('k')
        v = simple_validate(v)
        if v['valid']:
            v['nav'] = 'request_form'
            v['Supply'] = Supply
            v['srf'] = SupplyRequestForm()
            # v['medkit_delivery_events'] = [db.get(de) for de in v['MedKit'].delivery_events]
            # v['post_delivery_events'] = [db.get(de) for de in v['MedKit'].post_default.delivery_events]
            v['delivery_events'] = DeliveryEvent.all()

            html = render.page(self, "templates/volunteer/request_form.html", v)
            self.response.out.write(html)
        else:
            render.not_found(self)
    def post(self, post_code, kit_id):
        self.response.write.out('havent worked this out yet')
