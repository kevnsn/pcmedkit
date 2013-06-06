import sys
import os
from google.appengine.ext import db
from google.appengine.tools import bulkloader
from datetime import datetime
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import models

def date_handle(date_string):
    return datetime.strptime(date_string, "%m/%d/%Y")

def make_none(s):
    return None

def empty_list(s):
    return []

def utf_8_convert(s):
    return s.decode('utf-8')

def title(s):
    return s.title()

csv_to_db = {
    "Supply": [
        ('name', str),
        ('description', utf_8_convert),
        ('maximum', int),
        ],
    "DeliveryEvent": [
        ('name', str),
        ('date', date_handle),
        ('notes', str),
        ],
    "SupplyRequest": [
        ('supplies', empty_list),
        ('date', date_handle),
        ('quantities', empty_list),
        ('delivery_event', make_none), # ReferenceProperty
        ('status', title),
        ('status_notes', str), #TextProperty
        ('volunteer_notes', str), #TextProperty
        ],
    "Volunteer": [
        ('first_name', str),
        ('last_name', str),
        ('phone', str),
        ('email', str),
        ('trainee_input', str),
        ('project', str),
        ('cos', date_handle),
        ('sitelocation', str),
        ('notes', str), #TextProperty vs StringProperty??
        ('medkits', empty_list),
        ],
    "MedKit": [
        ('date_issued', date_handle),
        ('in_use', bool),
        ('volunteers', empty_list),
        ('supply_requests', empty_list),
        ('post_default', make_none), #ReferenceProperty
        ],
    "PostDefault": [
        ('slug', str),
        ('supplies', empty_list),
        ('post_admin', empty_list),
        ('region', str),
        ('post', str),
        ],
}

load_model = sys.argv[4].split("=")[-1]
print load_model

class PCMEDKIT_UPLOADER(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, load_model, csv_to_db[load_model])

loaders = [PCMEDKIT_UPLOADER]
