import os
import searchengine

pagelist=['https://en.wikipedia.org/wiki/Python']

crawler=searchengine.crawler('searchindex.db')
# crawler.createindextables( )
crawler.crawl(pagelist)

# DIR = 'toy'

# posts = [open(os.path.join(DIR, f)).read() for f in
# os.listdir(DIR)]

# print posts


# crawler=searchengine.crawler('searchindex.db')
# pages= ['http://kiwitobes.com/wiki/Categorical_list_of_programming_languages.html']
# crawler.crawl(pages)