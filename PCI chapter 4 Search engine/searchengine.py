import urllib2
from BeautifulSoup import *
from urlparse import urljoin
# Create a list of words to ignore
ignorewords=set(['the','of','to','and','a','in','is','it'])


class crawler:
  # Initialize the crawler with the name of database
  def __init__(self,dbname):
    self.listOfUrls = []
    pass
  def __del__(self):
    pass
  def dbcommit(self):
    pass


  # Auxilliary function for getting an entry id and adding
  # it if it's not present
  def getentryid(self,table,field,value,createnew=True):
    return None

  # Index an individual page
  def addtoindex(self,url,soup):
    print 'Indexing %s' % url
    self.listOfUrls.append(url)

  # Extract the text from an HTML page (no tags)
  def gettextonly(self,soup):
    return None

  # Separate the words by any non-whitespace character
  def separatewords(self,text):
    return None

  # Return true if this url is already indexed
  def isindexed(self,url):
    return url in self.listOfUrls
    # return False

  # Add a link between two pages
  def addlinkref(self,urlFrom,urlTo,linkText):
    pass


  def createindextables(self):
    pass

  # Starting with a list of pages, do a breadth
  # first search to the given depth, indexing pages
  # as we go
  # Create the database tables
  def crawl(self,pages,depth=2):
    for i in range(depth):
      newpages=[]
      for page in pages:
        # print "going for %s" % page
        try:
          c=urllib2.urlopen(page)
        except:
          print "Could not open %s" % page
          continue
        try:
          soup=BeautifulSoup(c.read())
          self.addtoindex(page,soup)

          links=soup('a')
          for link in links:
            # print 'processing link %s' % link

            if ('href' in dict(link.attrs)):
              url=urljoin(page,link['href'])
              if url.find("'")!=-1: continue

              url=url.split('#')[0]  # remove location portion
              if url[0:4]=='http' and not self.isindexed(url):
                newpages.append(url)

              linkText=self.gettextonly(link)
              self.addlinkref(page,url,linkText)

          self.dbcommit()
        except:
          print "Could not parse page %s" % page

      pages=newpages
      if(len(pages)>10): pages = pages[0:10]


