
from google.appengine.ext import db
from google.appengine.tools import bulkloader
import datetime
from models import *
def pl(x):
    if x == [] or x == None:
        return ''
    else:
        return ", ".join(x)

class AlbumExporter(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'sources',
            [('date', pl,  ""),
            ('date_added', pl,  ""),
            ('source', pl, ''),
            ('feed_url', pl, ''),
            ('title', pl, ''),
            ('link', pl, ''),
            ('description', pl, ''),
            ('relevance', pl, ''),
            ('content', pl, ''),
            ('tags_list', pl, ''),
            ('esil', pl, ''),
            ('report_list', pl, ''),
        ])
exporters = [AlbumExporter]
