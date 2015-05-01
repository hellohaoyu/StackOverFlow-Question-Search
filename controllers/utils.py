from urllib2 import *
import simplejson




def getSearchJSON(url):
	searchData = urlopen(url)
    searchJSON = simplejson.load(searchData)

    return searchJSON['response']['docs']

def getSearchURL(query):
	return "http://localhost:8983/solr/test/select?q=find+min+in+a+list+java&wt=json&indent=true&fl=*+score&rows=10"

def searchData(dateItems, query)
	# data = []
	# l = len(dateItems)
	url = getSearchURL(query)
	jsonRs = getSearchJSON(url)

	return jsonRs

