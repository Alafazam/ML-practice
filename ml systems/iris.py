import __main__
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# We load the data with load_iris from sklearn
from sklearn.datasets import load_iris
data = load_iris()

# load_iris returns an object with several fields
features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names

# plt.xkcd()
# print plt.get_plot_commands()
plt.figure(figsize=(16,9))
plt.autoscale(tight=True)

# subplot 1
plt.subplot(231)
# plt.minorticks_on()
for t in range(3):
	if t == 0:
		c = 'r'
		marker = '>'
	elif t == 1:
		c = 'g'
		marker = 'o'
	elif t == 2:
		c = 'b'
		marker = 'x'
	plt.scatter(features[target == t,0], features[target == t,1], marker=marker, c=c)
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.autoscale(tight=True)



plt.subplot(232)
for t in range(3):
	if t == 0:
		c = 'r'
		marker = '>'
	elif t == 1:
		c = 'g'
		marker = 'o'
	elif t == 2:
		c = 'b'
		marker = 'x'
	plt.scatter(features[target == t,0], features[target == t,2], marker=marker, c=c)
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[2])
plt.autoscale(tight=True)


plt.subplot(233)
for t in range(3):
	if t == 0:
		c = 'r'
		marker = '>'
	elif t == 1:
		c = 'g'
		marker = 'o'
	elif t == 2:
		c = 'b'
		marker = 'x'
	plt.scatter(features[target == t,0], features[target == t,3], marker=marker, c=c)
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[3])
plt.autoscale(tight=True)


plt.subplot(234)
for t in range(3):
	if t == 0:
		c = 'r'
		marker = '>'
	elif t == 1:
		c = 'g'
		marker = 'o'
	elif t == 2:
		c = 'b'
		marker = 'x'
	plt.scatter(features[target == t,1], features[target == t,2], marker=marker, c=c)
plt.xlabel(feature_names[1])
plt.ylabel(feature_names[2])
plt.autoscale(tight=True)

plt.subplot(235)
for t in range(3):
	if t == 0:
		c = 'r'
		marker = '>'
	elif t == 1:
		c = 'g'
		marker = 'o'
	elif t == 2:
		c = 'b'
		marker = 'x'
	plt.scatter(features[target == t,1], features[target == t,3], marker=marker, c=c)
plt.xlabel(feature_names[1])
plt.ylabel(feature_names[3])
plt.autoscale(tight=True)

plt.subplot(236)
for t in range(3):
	if t == 0:
		c = 'r'
		marker = '>'
	elif t == 1:
		c = 'g'
		marker = 'o'
	elif t == 2:
		c = 'b'
		marker = 'x'
	plt.scatter(features[target == t,2], features[target == t,3], marker=marker, c=c)
plt.xlabel(feature_names[2])
plt.ylabel(feature_names[3])
# plt.savefig(__main__.__file__+"_plot.png")
plt.show()
