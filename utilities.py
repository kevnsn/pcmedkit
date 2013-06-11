from google.appengine.ext import db
from models import MedKit, SupplyRequest


## This Code wouldn't have been so confusing if we had modeled the data right... oops
# def sr_improver(suppy_request_list):
#     sply_requests = [db.get(sr_key) for sr_key in suppy_request_list]
#     sorted_sply_requests = sorted(sply_requests, key=lambda sr: sr.date, reverse=True)
#     improved_supply_requests = []
#     for sr in sorted_sply_requests:
#         index = 0
#         request_details = []
#         for supply in sr.supplies:
#             supply_rec = db.get(supply)
#             quantity = sr.quantities[index]
#             request_details.append({'sply': supply_rec, "qty": quantity})
#             index += 1
#         sr.request_details = request_details
#         improved_supply_requests.append(sr)
#     return improved_supply_requests


def sr_improver(suppy_request_query):
    q_processed = []
    for supply_request in suppy_request_query:
        supply_objects = []
        for supply_item in supply_request.supplies:
            supply_objects.append(db.get(supply_item))
        supply_request.supply_objects = supply_objects
        q_processed.append(supply_request)
    return q_processed

#  For compatability, Run this in the Interactive Console of your Dev Server
def fix_medkit_request_relationship():
    num_fixed = 1
    for kit in MedKit.all():
        for request in kit.supply_requests:
            old = db.get(request)
            if old == None:
                continue
            new = SupplyRequest(
                date = old.date,
                delivery_event = old.delivery_event,
                quantities = old.quantities,
                supplies = old.supplies,
                status = old.status,
                status_notes = old.status_notes,
                volunteer_notes = old.volunteer_notes,
                medkit = kit,
                post_default = kit.post_default,
            )
            new.put()
            old.delete()
            num_fixed += 1
    return str(num_fixed) + " supply requests reinputed into the database!"