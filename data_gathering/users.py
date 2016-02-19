import os
from bs4 import BeautifulSoup
from Profile import *
import shelve
import pprint


FULL_NAME_CLASS = "vcard-fullname"
USERNAME_CLASS = "vcard-username"
CONTRIBURIONS_COUNT_CLASS = "contrib-number"
VCARD_STATS_CLASS = "vcard-stat-count"


cwd = os.getcwd()

user_profiles_dir = os.path.join(cwd,'crawled','users')

# get list of all files

files = os.listdir(user_profiles_dir)

# print files
# files = files[:2]
users = []
count = 0
# shelfFile = shelve.open('users_shelf')


for f in files:
	read = open(os.path.join(user_profiles_dir,f),'r').read()
	soup = BeautifulSoup(read, 'html.parser')
	user = Profile(soup)
	users.append(user)
	count += 1
	print "Profiles scanned %d, Last scanned %s" % (count, user.name)	

# shelfFile['users'] = users
# shelfFile.close()
fileObj = open('user_data.py', 'w')
fileObj.write('users = ' + pprint.pformat(users).encode('utf8') + '\n')
fileObj.close()
print "all %d written" % count


dataset = []