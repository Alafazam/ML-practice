import feedparser
import re


# returns title dictionary of word counts for an RSS feed

def getwrodcounts(url):
	try:
		d = feedparser.parse(url)

		# wc = {}

		#loop over all entries
		# for e in d.entries:
		# 	if 'summary' in e :
		# 		summary = e.summary
		# 	else : summary = e.discription

		# 	# Extract list of words
		# 	words = getwords(e.title+ ' ' + summary)

		# 	for word in words :
		# 		wc.setdefault(word,0)
		# 		wc[word]+= 1

		if hasattr(d.feed, 'title'):
			print url , d.feed.title
			print ''
		else :
			print url

	except Exception, e:
		# raise e
		pass


def getwords(html):
	# remove all html tags
	txt = re.compile(r'<[^>]+>').sub('',html)

	#split words by all non alpha characters
	words = re.compile(r'[^A-Z^a-z]+').split(txt)

	#convert to lowercase
	return [word.lower() for word in words if word!='']

for feedurl in file('feedlist.txt'):
	getwrodcounts(feedurl)
