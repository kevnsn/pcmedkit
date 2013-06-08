from google.appengine.ext import db
from random import randint

class Volunteer(db.Model):
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    phone = db.PhoneNumberProperty(required=False)
    email = db.EmailProperty(required=False)
    trainee_input = db.StringProperty(required=False)
    project = db.StringProperty(required=True)
    cos = db.DateTimeProperty(required=False)
    sitelocation = db.TextProperty(required=False)
    notes = db.TextProperty(required=False)
    medkits = db.ListProperty(db.Key)

class DeliveryEvent(db.Model):
    name = db.StringProperty(required=True)
    date = db.DateTimeProperty(required=False)
    notes = db.TextProperty(required=False)

class Supply(db.Model):
    name = db.StringProperty(required=True)
    description = db.StringProperty(required=True)
    maximum = db.IntegerProperty(required=False)

class SupplyRequest(db.Model):
    supplies = db.ListProperty(db.Key)
    date = db.DateTimeProperty(required=False)
    quantities = db.ListProperty(int)
    delivery_event = db.ReferenceProperty(DeliveryEvent)
    status = db.StringProperty(required=True, choices=set(["Requested", "In Transit", "Completed", "See Notes"]), default="Requested")
    status_notes = db.TextProperty(required=False)
    volunteer_notes = db.TextProperty(required=False)

class PostDefault(db.Model):
    slug = db.StringProperty(required=True)
    supplies = db.ListProperty(db.Key)
    post_admin = db.ListProperty(str)
    region = db.StringProperty(required=True, choices=set(["AFR", "IAP", "EMA", "Other"]))
    post_name = db.StringProperty(required=True)
    delivery_events = db.ListProperty(db.Key)


class MedKit(db.Model):
    code = db.StringProperty(required=False)
    date_issued = db.DateTimeProperty(required=False)
    in_use = db.BooleanProperty(required=False)
    volunteer = db.ReferenceProperty(Volunteer)
    supply_requests = db.ListProperty(db.Key)
    post_default = db.ReferenceProperty(PostDefault)
    delivery_events = db.ListProperty(db.Key)
    def put(self):
        key = super(MedKit, self).put()
        if self.code is None:
            unique = False
            while unique == False:
                key_as_str = str(self.key())
                key_length = len(key_as_str)
                rn1 = randint(10, 999)
                rn2 = randint(10, 999)
                rc1 = key_as_str[randint(0, key_length - 1)]
                rc2 = key_as_str[randint(0, key_length - 1)]
                code = "%s%s-%s-%s" % (rc1, rc2, rn1, rn2)
                if MedKit.all().filter('code =', code).count() == 0:
                    unique = True
            self.code = code
            key = super(MedKit, self).put()
        return key



