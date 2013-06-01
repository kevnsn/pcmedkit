import webapp2
import home

app = webapp2.WSGIApplication([('/', home.main),
                               ], debug=True)
