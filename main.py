# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

def find_suspect(content):
    length = len(content)
    res = ""
    for i in range(length - 7):
        if i < length - 12:
            # Gender female
            if content[i:(i + 12)] == "TGAAGGACCTTC":
                res += "Gender: female<br>"
            # Gender male
            if content[i:(i + 12)] == "TGCAGGAACTTC":
                res += "Gender: male<br>"
        if i < length - 11:
            # Hair color black
            if content[i:(i + 11)] == "CCAGCAATCGC":
                res += "Hair color: black<br>"
            # Hair color blonde
            if content[i:(i + 11)] == "TTAGCTATCGC":
                res += "Hair color: blonde<br>"
        if i < length - 10:
            # Hair color brown
            if content[i:(i + 10)] == "GCCAGTGCCG":
                res += "Hair color: brown<br>"
            # Eye color blue
            if content[i:(i + 10)] == "TTGTGGTGGC":
                res += "Eye color: blue<br>"
            # Eye color green
            if content[i:(i + 10)] == "GGGAGGTGGC":
                res += "Eye color: green<br>"
            # Eye color brown
            if content[i:(i + 10)] == "AAGTAGTGAC":
                res += "Eye color: brown<br>"
        if i < length - 9:
            # Race white
            if content[i:(i + 9)] == "AAAACCTCA":
                res += "Race: white<br>"
            # Race black
            if content[i:(i + 9)] == "CGACTACAG":
                res += "Race: black<br>"
            # Race asian
            if content[i:(i + 9)] == "CGCGGGCCG":
                res += "Race: asian<br>"
        if i < length - 8:
            # Face shape oval
            if content[i:(i + 8)] == "AGGCCTCA":
                res += "Face: oval<br>"
        if i < length - 7:
            # Face shape square
            if content[i:(i + 7)] == "GCCACGG":
                res += "Face: square<br>"
            # Face shape round
            if content[i:(i + 7)] == "ACCACAA":
                res += "Face: round<br>"
    return res

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):

    def get(self):
        return self.render_template("write_dna.html")

class SuspectHandler(BaseHandler):
    def post(self):
        val = self.request.get("get_dna")
        res = "Suspect characteristics:<br><br>"
        res += find_suspect(val)
        self.write(res)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/suspect', SuspectHandler)
], debug=True)
