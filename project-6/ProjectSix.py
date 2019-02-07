# Project Six - Web Scraping
# NAME: Audrey Gu
# OTHER COMMENTS: Due to the sheer amount of linked content on most websites, I would advise against running my URL or email scraping functions beyond the depth of 1 or 2 for complex sites (it should work, but will take an incredibly long time given that they reference hundreds of other sites - test with The Verge at depth 0 to see what I mean).
# Further, my email scraping function is only capable of determining whether or not a text string fulfills the syntactical requirements for a valid email address, regardless of whether such an address actually exists. I don't believe that was in the scope of this project, but I'd thought I'd mention it anyway. Invalid URLs are less common given the regex I've used, but the same applies to those as well.
# Test sites: http://www.donnadietz.com, http://www.american.edu/careercenter/Staff-Directory.cfm, and http://www.theverge.com.

import urllib
import re

def urlToString(urlName):
	contents = "Access Attempt Failed"
	try:
		tmp = urllib.urlopen(urlName)
		contents = tmp.read()
	except:
		pass
	return contents


def contentsToUrlList(contents):
	urlExtract = re.findall("https?:\/\/[\w.\/\-\(\)]+\.[\w.\/\-\(\)]+\.[\w.\/\-\(\)]+[a-zA-Z0-9]", contents)
	return urlExtract


def contentsToEmailList(contents):
	emailExtract = re.findall("[\w\.]+@[\w\.]+\.[\w]+", contents)
	return emailExtract


def scrapeUrlToList(newUrls, L):
	for i in len(range(newUrls)):
		L.append(newUrls[i])


def scrapeUrlsFrom(parentUrl, maxSites):
	print "Visiting... "+str(parentUrl)
	tmp = urlToString(parentUrl)
	pool = contentsToUrlList(tmp)
	if maxSites:
		for i in range(len(pool)):
			extendedSearch = scrapeUrlsFrom(pool[i], maxSites-1)
			pool.extend(extendedSearch)
	return list(set(pool))


def scrapeEmailsFrom(parentUrl, maxSites):
	pool = []
	checkList = scrapeUrlsFrom(parentUrl, maxSites)
	for i in range(len(checkList)):
		tmp = urlToString(checkList[i])
		search = contentsToEmailList(tmp)
		if search:
			print "Valid addresses found: "+str(search)
		pool.extend(search)
	print ""
	return list(set(pool))
