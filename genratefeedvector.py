import feedparser
import re


# returns title dictionary of word counts for an RSS feed

def getwrodcounts(url):
	d = feedparser.parse(url)
	wc = {}

	#loop over all entries
	for e in d.entries:
		if 'summary' in e :
			summary = e.summary
		else : summary = e.discription

		# Extract list of words
		words = getwords(e.title+ ' ' + summary)

		for word in words :
			wc.setdefault(word,0)
			wc[word]+= 1

	return d.feed.title, wc

def getwords(html):
	# remove all html tags
	txt = re.compile(r'<[^>]+>').sub('',html)

	#split words by all non alpha characters
	words = re.compile(r'[^A-Z^a-z]+').split(txt)

	#convert to lowercase
	return [word.lower() for word in words if word!='']


apcount = {}
wordscount = {}

for feedurl in file('feedlist.txt'):
	title,wc = getwrodcounts(feedurl)
	wordscount[title] = wc
	for word,count in wc.items():
		apcount.setdefault(word,0)
		if count > 1 :
			apcount[word]+= 1

wordlist = {}
for w,bc in apcount.items():
	frac = float(bc)/len(feelist)
	if frac > 0.1 and frac < 0.5: wordlist.append(wc)


out = file('blogdata.txt','w')
out.write("Blog")
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordscount.items():
	out.write(blog)
	for word in wordlist:
		if word in wc: 
			out.write('\t%d' % wc[word])
		else: out.write('\t0')
	out.write('\n')	 