from urllib2 import *
# import json as simplejson
from django.utils import simplejson
import logging

def getSearchJSON(url):
	searchData = urlopen(url)
	searchJSON = simplejson.load(searchData)
	return searchJSON['response']['docs']

def getSearchURL(query):
	# dataItems = ['Id', 'Title', 'Tags']
	logging.info(query)
	query = re.sub(r"[^\w\s]", '', query)
	query = re.sub(r"\s+", '+', query)
	logging.info(query)
	# tag = re.sub(r"\s+",'+',tag)
	# queryURL = "http://localhost:8983/solr/test/select?q=Title%3A+"+query+"+OR+Tags%3A+"+tag+"+&wt=json&indent=true&row=100"
	# queryURL = "http://localhost:8983/solr/test/select?q=Title%3A+"+query+"&fl=Id%2C+Title%2C+Tags&wt=json&indent=true&row=10"
	queryURL = "http://ec2-52-7-48-130.compute-1.amazonaws.com:8983/solr/test/select?q=Title%3A+"+query+"&fl=Id%2C+Title%2C+Tags&wt=json&indent=true&row=10"

	logging.info(queryURL)
	return queryURL
	
	# return "http://localhost:8983/solr/test/select?q=find+min+in+a+list+java&wt=json&fl=Title%2C+Id%2C+Tags&indent=true&rows=10"
# input questions, dateitems and query are used to create query url
def searchData(query = None):
	url = getSearchURL(query)
	jsonRs = getSearchJSON(url)
	return jsonRs

