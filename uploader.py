
from google.appengine.ext import db
from google.appengine.tools import bulkloader
import datetime
from models import *
def pl(x):
    if x == [] or x == None:
        return ''
    else:
        return ", ".join(x)

class SupplyUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'Supply',
            [('date', pl,  ""),
        ])

class DeliveryEventUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'DeliveryEvent',
            [('date', pl,  ""),
        ])

class SupplyRequestUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'SupplyRequest',
            [('date', pl,  ""),
        ])

class VolunteerUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'Volunteer',
            [('date', pl,  ""),
        ])

class MedBoxUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'MedBox',
            [('date', pl,  ""),
        ])
class PostDefaultUploader(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'PostDefault',
            [('date', pl,  ""),
        ])

exporters = [AlbumExporter]
