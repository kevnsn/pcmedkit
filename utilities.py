from google.appengine.ext import db

def sr_improver(suppy_request_list):
    sply_requests = [db.get(sr_key) for sr_key in suppy_request_list]
    sorted_sply_requests = sorted(sply_requests, key=lambda sr: sr.date, reverse=True)
    improved_supply_requests = []
    for sr in sorted_sply_requests:
        index = 0
        request_details = []
        for supply in sr.supplies:
            supply_rec = db.get(supply)
            quantity = sr.quantities[index]
            request_details.append({'sply': supply_rec, "qty": quantity})
            index += 1
        sr.request_details = request_details
        improved_supply_requests.append(sr)
    return improved_supply_requests
