import webapp2
import home
app = webapp2.WSGIApplication([('/', home.vol),
                               ('/volunteer',home.vol),
                               ('/officer',home.sec),
                               ('/post/',siteadmin.main),
                               ('/pcs/',pcv.main),
                               ], debug=True)

                          
