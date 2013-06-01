from google.appengine.ext import db

class Volunteer(db.Model):
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    phone = db.PhoneNumberProperty(required=False)
    email = db.EmailProperty(required=False)
    trainee_input = db.StringProperty(required=True)
    project = db.StringProperty(required=True)
    cos = db.DateTimeProperty(required=False)
    sitelocation = db.TextProperty(required=False)
    notes = db.TextProperty(required=False)
    medboxs = db.ListProperty(db.Key)

class MedBox(db.Model):
    code = db.StringProperty(required=False)
    date_issued = db.DateTimeProperty(required=False)
    in_use = db.BooleanProperty(required=False)
    volunteers = db.ListProperty(db.Key)
    supply_requests = db.ListProperty(db.Key)
    regional_defualts = db.ListProperty(db.Key)
    def put(self):
        key = super(articles, self).put()
        if medbox.mdid is None:
            medbox.mdid = str(self.key())[:2] + str(self.id())
            key = super(articles, self).put()
        return key

class DeliveryEvent(db.Model):
    name = db.StringProperty(required=True)
    date = db.DateTimeProperty(required=False)
    notes = db.TextProperty(required=False)

class Supply(db.Model):
    name = db.StringProperty(required=True)
    packaging = db.StringProperty(required=True)
    maximum = db.IntegerProperty(required=False)

class SupplyRequest(db.Model):
    supplies = db.ListProperty(db.Key)
    date = db.DateTimeProperty(required=False)
    quantities = db.ListProperty(int)
    delivery_event = db.ReferenceProperty(DeliveryEvent)
    status = db.StringProperty(required=True, choices=set(["Requested", "In Transit", "Completed", "See Notes"]), default="Requested")
    status_notes = db.TextProperty(required=False)
    pcv_notes = db.TextProperty(required=False)

class RegionalDefault(db.Model):
    supplies = db.ListProperty(db.Key)
    packaging = db.StringProperty(required=True)
    status = db.StringProperty(required=True, choices=set(["AFR", "IAP", "EMA", "Other"]))
    post = db.StringProperty(required=True)
