import webapp2
import render

class landing(webapp2.RequestHandler):
    def get(self):
        html = ''
        html = '<h1>Welcome</h1>'
        html += '<p>Visit the <a href="/post/xxx/newmedkit">"Assign Medbox Form"</a> for a mini demo.</p>'
        v = {'dumb_content': html}
        html = render.page(self, "templates/base.html",v)
        self.response.out.write(html)


class main(webapp2.RequestHandler):
    def get(self, site):
        html = render.page(self, "templates/volunteer/home.html",{})
        self.response.out.write(html)
    def post(self, site):
        html = render.page(self, "templates/volunteer/home.html",{})
        self.response.out.write(html)

class form(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'position': 'Medical Officer',
            'verb': 'extremely enjoy'
        }
        html = render.page(self, "templates/volunteer/supply_form.html",template_values)
        self.response.out.write(html)
