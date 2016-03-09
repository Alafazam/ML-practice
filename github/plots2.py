import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from stats import *


def convert(k):
	array = []
	for x in k:
		y = []
		y.append(x["followers"])
		y.append(x["total_contributions"])
		y.append(x["longest_streak"])
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
y = convert(users[:20])
y = np.array(y)

# print y

df2 = pd.DataFrame(y, columns=['followers', 'total_contributions', 'longest_streak'])
df2.plot(kind='bar');
plt.show()

