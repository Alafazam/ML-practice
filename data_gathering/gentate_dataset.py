import users
out = file('githubprofiles.txt','w')

out.write("name\t\t\tusername\t\t\ttotal_contributions\tlongest_streak\tcurrent_streak\tfollowers\tstarred\tfollowing\n")
for x in range(len(users)):
	t = "%s\t\t\t%s\t\t\t%s\t%s\t%s\t%s\t%s\t%s\n" \
	%(user['name'], user['username'], user['total_contributions'], user['longest_streak'], user['current_streak'], user['followers'], user['starred'], user['following'])
	out.write(t)

out.close()