import scipy as sp
import matplotlib.pyplot as plt
from stats import *


def convert(k):
	array = []
	for x in k:
		y = []
		y.append(x["starred"])
		y.append(x["following"])
		array.append(y)
	return array

data = convert(users)
data = sp.array(data)
# print x

x = data[:,0]
y = data[:,1]
# print x

x = x[x<100]
y = y[x<100]

x = x[y<100]
y = y[y<100]


# plot the (x,y) points with dots of size 10
plt.scatter(x, y, s=10)
plt.title("Following vs starred")
plt.xlabel("Starred")
plt.ylabel("Following")

plt.autoscale(tight=True)
# draw a slightly opaque, dashed grid
# plt.grid(True, linestyle='-', color='0.75')

def error(f, x, y):
	return sp.sum((f(x)-y)**2)



fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 2, full=True)
print("Model parameters: %s" % fp1)
f1 = sp.poly1d(fp1)
fx = sp.linspace(0,x[-1], 1000) # generate X-values for plotting
print(error(f1, x, y))
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")
# plt.show()

f2p = sp.polyfit(x, y, 2)

f2 = sp.poly1d(f2p)

print(error(f2, x, y))

plt.plot(fx, f2(fx), linewidth=4)
plt.legend(["d=%i" % f2.order], loc="upper left")
plt.show()
