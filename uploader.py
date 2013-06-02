
from google.appengine.ext import db
from google.appengine.tools import bulkloader
from datetime import datetime
from models import *

def pl(x):
    if x == [] or x == None:
        return ''
    else:
        return ", ".join(x)

class SupplyUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'Supply',
            [('name', str,  ""),
            ('description', str,  ""),
            ('maximum', int,  1),
        ])

class DeliveryEventUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'DeliveryEvent',
            [('name', str,  ""),
            ('date', datetime.strptime("%m/%d/%Y"),  ""),
            ('notes', str,  ""),
        ])

class SupplyRequestUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'SupplyRequest',
            [('supplies', list,  []),
            ('date', datetime.strptime("%m/%d/%Y"),  ""),
            ('quantities', list,  []),
            ('delivery_event', str,  ""), # ReferenceProperty
            ('status', str,  "Requested"),
            ('status_notes', str,  ""), #TextProperty
            ('volunteer_notes', str,  ""), #TextProperty
        ])

class VolunteerUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'Volunteer',
            [('first_name', str,  ""),
            ('last_name', str,  ""),
            ('phone', str,  ""), #PhoneNumberProperty
            ('email', str,  ""), #EmailProperty
            ('trainee_input', str,  ""),
            ('project', str,  ""),
            ('cos', datetime.strptime("%m/%d/%Y"),  ""),
            ('sitelocation', str,  ""), #TextProperty vs StringProperty??
            ('notes', str,  ""), #TextProperty vs StringProperty??
            ('medboxs', list,  []),
        ])

class MedBoxUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'MedBox',
            [('code', str,  ""),
            ('date_issued', datetime.strptime("%m/%d/%Y"),  ""),
            ('in_use', bool,  False),
            ('volunteers', list,  []),
            ('supply_requests', list,  []),
            ('post_default', list,  []), #ReferenceProperty
        ])

class PostDefaultUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'PostDefault',
            [('slug', str,  ""),
            ('supplies', list,  []),
            ('post_admin', list,  []),
            ('region', str,  ""),
            ('post', str,  ""),
        ])

exporters = [AlbumExporter]
