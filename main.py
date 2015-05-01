'''
@author: Haoyu Chen
@contact: hc6as@virginia.edu
'''
import logging
from controllers import Search
import webapp2
import jinja2
import os

# Initialize the jinja environment
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info("Get MainPage")
        template_value = {}
        template_value['data'] = [{'Title': "This is question title"}]
        template = jinja_environment.get_template('index.html')
        self.response.write(template.render(template_value))

app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
        ('/Search', Search.SearchHandler)
    ], debug=True)

