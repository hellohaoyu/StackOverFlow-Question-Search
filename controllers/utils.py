from urllib2 import *
# import json as simplejson
from django.utils import simplejson

def getSearchJSON(url):
	searchData = urlopen(url)
	searchJSON = simplejson.load(searchData)
	return searchJSON['response']['docs']

def getSearchURL(query):
	return "http://localhost:8983/solr/test/select?q=find+min+in+a+list+java&wt=json&fl=Title%2C+Id%2C+Tags&indent=true&rows=10"

# input questions, dateitems and query are used to create query url
def searchData(question = None, dateItems = None, query = None):
	url = getSearchURL(query)
	jsonRs = getSearchJSON(url)
	return jsonRs

