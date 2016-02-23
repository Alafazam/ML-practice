import os
from bs4 import BeautifulSoup
from Profile import *
import shelve
import pprint





# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DON'T USE THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! USE GITHUB API !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


for i in range(46):
	url = "https://github.com/search?o=desc&p=%d&q=followers%\3A%\3E1000&ref=searchresults&s=followers&type=Users" % ()
	read = open(os.path.join(user_profiles_dir,f),'r').read()
	soup = BeautifulSoup(read, 'html.parser')
	user = Profile(soup)
	users.append(user)
	count += 1
	print "Profiles scanned %d, Last scanned %s has %s followers" % (count, user.name, user.followers)	

# shelfFile['users'] = users
# shelfFile.close()
fileObj = open('user_data.py', 'w')
fileObj.write('users = ' + pprint.pformat(users) + '\n')
fileObj.close()
print "all %d written" % count

# out = file('githubprofiles.txt','w')

# out.write("id\t\ttotal_contributions\t\tlongest_streak\t\tcurrent_streak\t\tfollowers\t\tstarred\t\tfollowing\t\t\n")
# count = 0
# for user in users:
# 	t = "%s 		%s						%s					%s					%s				%s			%s\n" \
# 	%(count, user.total_contributions, user.longest_streak, user.current_streak, user.followers, user.starred, user.following)
# 	out.write(t)
# 	count += 1
# out.close()
