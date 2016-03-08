import __main__
import numpy as np
from scipy.stats import kendalltau
import seaborn as sns
import matplotlib.pyplot as plt
from stats import *
sns.set(style="ticks")

def ripu_(k,s):
	return [x[s] for x in k]

rs = np.random.RandomState(1000)
# print rs
# x = rs.gamma(12, size=60)
# y = 2 + rs.gamma(60,size=60)
# x = rs.gamma(2, size=1000)

# print 'y = '+ str(y)

# graph = sns.jointplot(x, y, kind="hex", stat_func=kendalltau, color="#4CB391")



y = ripu_(users,'followers')
m = mean(users,'followers')
# y = [(x+0.0)/m for x in y]
y = np.array(y)

x = np.random.normal(size=20)
# print 'x = '+ str(x)
# print 'y = '+ str(y)
graph = sns.distplot(y);


# sns.plt.savefig(__main__.__file__+".png")
# graph.pyplot.show()
sns.plt.show()

# print mean(users,'followers',top=20)

