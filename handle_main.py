import webapp2
import home, superadmin, postadmin, volunteer

app = webapp2.WSGIApplication([('/',home.landing),
                               ('/regions',home.landing),
                               (r'/post/(.+)/medkit',volunteer.landing),
                               (r'/post/(.+)/request',volunteer.request_form),
                               (r'/post/(.+)/check_status',volunteer.status),
                               (r'/post/(.+)',postadmin.landing),
                               ], debug=True)

admin = webapp2.WSGIApplication([('/admin', superadmin.main)], debug=True)

siteadmin = webapp2.WSGIApplication([
                               (r'/post/(.+)/admin', postadmin.landing),
                               (r'/post/(.+)/admin/supplies', postadmin.supply_form),
                               (r'/post/(.+)/admin/requests', postadmin.requests_table),
                               (r'/post/(.+)/admin/assign_medkit', postadmin.medkit),
                               ], debug=True)
