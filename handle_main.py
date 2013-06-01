import webapp2
import home
app = webapp2.WSGIApplication([('/', home.vol),
                               ('/volunteer',home.vol),
                               ('/officer',home.sec)], debug=True)

                          
