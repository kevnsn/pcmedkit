import webapp2
import home, superadmin, siteadmin, volunteer

app = webapp2.WSGIApplication([('/',volunteer.landing),
                               (r'/post/(.+)/medkit',volunteer.main),
                               ('/request',volunteer.form),
                               (r'/post/(.+)',siteadmin.main),
                               ], debug=True)

admin = webapp2.WSGIApplication([('/admin', superadmin.main)], debug=True)

siteadmin = webapp2.WSGIApplication([
                               (r'/post/(.+)/supplyform', siteadmin.form),
                               (r'/post/(.+)/newmedkit', siteadmin.boxform),
                               ], debug=True)
