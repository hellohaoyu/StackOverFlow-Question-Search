import logging
import webapp2
import jinja2
import utils
from django.utils import simplejson as json


class SearchHandler(webapp2.RequestHandler):
	def post(self):
		inputQuestion = self.request.get("question")
		jsonQuestions = utils.searchData(inputQuestion)
		jsonQuestions = jsonQuestions[0:5]
		self.response.write(json.dumps(jsonQuestions, ensure_ascii=False))