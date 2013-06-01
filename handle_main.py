import webapp2
import home
app = webapp2.WSGIApplication([('/', home.vol),
                               ('/post/(?P<site>).+/medkit',volunteer.main),
                               ('/request',volunteer.form),
                               ('/post/(?P<site>).+',siteadmin.main),
                               ], debug=True)

                          
admin = webapp2.WSGIApplication([('/admin', superadmin.main)], debug=True)
                          
siteadmin = webapp2.WSGIApplication([
                               ('/post/(?P<site>).+/supplyform',siteadmin.form),
                               ('/post/(?P<site>).+/newmedkit',siteadmin.boxform)
                               ], debug=True)
