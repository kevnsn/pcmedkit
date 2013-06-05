import webapp2
import home, superadmin, postadmin, volunteer

app = webapp2.WSGIApplication([('/',home.landing),
                               ('/regions',home.landing),
                               (r'/post/(.+)/medkit',volunteer.landing),
                               (r'/post/(.+)/request',volunteer.request_form),
                               (r'/post/(.+)/check_status',volunteer.status),
                               ], debug=True)

admin = webapp2.WSGIApplication([('/admin', superadmin.main)], debug=True)

siteadmin = webapp2.WSGIApplication([(r'/post/(.+)/admin/supplies', postadmin.supply_form),
                               (r'/post/(.+)/admin/requests', postadmin.requests_table),
                               (r'/post/(.+)/admin/assign_medkit', postadmin.medkit),
                               (r'/post/(.+)/admin', postadmin.requests_table),
                               ], debug=True)
