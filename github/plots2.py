import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from stats import *
from matplotlib import cm

def convert(k):
	array = []
	for x in k:
		y = []
		y.append(x["followers"])
		# y.append(x["username"])
		# y.append(x["following"])
		y.append(x["total_contributions"])
		# y.append(x["longest_streak"])
		# y.append(x["current_streak"])
		array.append(y)
	return array
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
# df = df.cumsum()
# print df2
# print np.random.rand(10, 4)
# y = ripu_(users,'followers')
# m = mean(users,'followers')
# y = [(x+0.0)/m for x in y]
# y = convert(users)
# y = np.array(y)
# print y
# df2 = pd.DataFrame(y, columns=['followers', 'total_contributions', 'longest_streak'])
# df2.plot(kind='bar');
# plt.show()
# top_f = sorted(users, key=lambda x: x['followers'], reverse=True)[:50]
top_f = sorted(users, key=lambda x: x['followers'])

t = len(users)
k = 100
# top_f = users[t/2-k:t/2+k]
# top_f = users
# print top_f
y = convert(top_f)
y = np.array(y)

# print y
df3 = pd.DataFrame(y,columns=['followers','total_contributions'])
# print df3
# df3 = df3.cumsum()
# df3[' '] = pd.Series(list(range(len(df3))))
# df3.plot(colormap=cm.cubehelix)

# df3.plot(kind='hist',bins=50)
# df3.plot(kind='area', stacked=False)
# df3.plot(kind='hexbin', x='followers', y='total_contributions')


df3.plot(x='followers', y='total_contributions', kind='area')
# df3.hist(bins=50)

# df3['total_contributions'].diff().hist()

# df3.diff().hist(bins=50)

plt.show()
