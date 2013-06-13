import webapp2
import render


class main(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Peace Corps Volunteer',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/superadmin/home.html",template_values)
        self.response.out.write(html)
