import logging
import webapp2
import jinja2
import utils
from django.utils import simplejson as json


class SearchHandler(webapp2.RequestHandler):
	def post(self):
		inputTitle = self.request.get("inputTitle")
		#recomd = TagRecommender()
		#recomdTags = recomd.tagRecommender(inputTitle)

		jsonQuestions = utils.searchData(query = inputTitle)
		jsonQuestions = jsonQuestions[0:5]
		self.response.write(json.dumps(jsonQuestions, ensure_ascii=False))

class TagRecommender(object):
	"""docstring for TagRecommender"""
	def tagRecommender(inputTitle):
		return None
		