import pprint
from clusters import *
from pearson_corelation2 import *

from user_data import *

# def get_ints(k):
# 	return { 'username': k['username'], 'total_contributions' : int(k['total_contributions']), 'longest_streak' : int(k['longest_streak']), 'current_streak' : int(k['current_streak']), 'followers' : int(k['followers']), 'starred' : int(k['starred']), 'following' : int(k['following'])}
# def convert_strings_to_ints():
# 	newlist = [ get_ints(x) for x in users]
# 	fileObj = open('user_data.py', 'w')
# 	fileObj.write('users = ' + pprint.pformat(newlist) + '\n')
# 	fileObj.close()

def rip_(k,s):
	return [{'us': x['username'], s : x[s]} for x in k]


def show_stats(users):	
	# top 10 most followed users in github team.
	top_f = sorted(users, key=lambda x: x['followers'], reverse=True)[:10]
	print 'followers \n', pprint.pformat(rip_(top_f,'followers'))

	# top 10 users with most contributions in github team.
	top_contri = sorted(users, key=lambda x: x['total_contributions'], reverse=True)[:10]
	print 'total_contributions \n', pprint.pformat(rip_(top_contri,'total_contributions'))

	# top 10 users with longest streak in github team.
	top_longest_streak = sorted(users, key=lambda x: x['longest_streak'], reverse=True)[:10]
	print 'longest_streak \n', pprint.pformat(rip_(top_longest_streak,'longest_streak'))

	# top 10 users with longest current streak in github team.
	top_longest_current_streak = sorted(users, key=lambda x: x['current_streak'], reverse=True)[:10]
	print 'current_streak \n', pprint.pformat(rip_(top_longest_current_streak,'current_streak'))

	# top 10 users following most repos in github team.
	top_following = sorted(users, key=lambda x: x['following'], reverse=True)[:10]
	print 'following \n', pprint.pformat(rip_(top_following,'following'))


def convert_to_row_cols(k):
	rows = []
	cols = []
	for x in k:
		row = []
		for y in x:
			if y == 'username':
				cols.append(x[y])
			else:
				row.append(x[y])
		rows.append(row)		
	return rows,cols

rows, cols = convert_to_row_cols(users)
# print rows[0],cols[0]
# print len(rows)

# clust = kcluster(rows,k=7)
# print kclust

# clust = hcluster(rows)
# drawdendrogram(clust,cols,jpeg='randomK.jpg')


