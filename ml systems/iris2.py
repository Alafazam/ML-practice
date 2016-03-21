import __main__
from matplotlib import pyplot as plt
import numpy as np
import random
# We load the data with load_iris from sklearn
from sklearn.datasets import load_iris
data = load_iris()

# load_iris returns an object with several fields

observations = []
best_fit_data = []
for e in range(0,5):
	# print e
	features = data.data
	feature_names = data.feature_names
	target = data.target
	target_names = data.target_names
	labels = target_names[target]

	randomz = [x for x in range(0,150)]
	random.shuffle(randomz)
	randomz = randomz[:10]
	randomz = np.array(randomz)

	test_features = features[randomz]
	test_labels = labels[randomz]
	test_target = target[randomz]

	features = features[~randomz]
	labels = labels[~randomz]
	target = target[~randomz]

	plength = features[:, 2]
	is_setosa = (labels == 'setosa')
	min_non_setosa = plength[~is_setosa].min()
	# max_setosa = plength[is_setosa].max()

	# separating setosa
	features = features[~is_setosa]
	labels = labels[~is_setosa]

	# Build a new target variable, is_virginica
	is_virginica = (labels == 'virginica')

	# Initialize best_acc to impossibly low value
	best_fi = None
	best_t = None
	best_reverse = None
	best_acc = -1.0
	for fi in range(features.shape[1]):
		# We are going to test all possible thresholds
		thresh = features[:,fi]
		for t in thresh:
			# Get the vector for feature `fi`
			feature_i = features[:, fi]
			# apply threshold `t`
			pred = (feature_i > t)
			acc = (pred == is_virginica).mean()
			rev_acc = (pred == ~is_virginica).mean()
			if rev_acc > acc:
				reverse = True
				acc = rev_acc
			else:
				reverse = False

			if acc > best_acc:
				best_acc = acc
				best_fi = fi
				best_t = t
				best_reverse = reverse
	result = []
	best_f_data = [best_t,best_fi]
	best_fit_data.append(best_f_data)
	# print 'best_t',best_t
	# print "best_acc",best_acc
	# print "best_fi",best_fi
	for f in test_features:
		if f[2] < min_non_setosa:
			result.append(0)
		else:
			ans = False
			if f[best_fi] > best_t:
				ans  = True
			if best_reverse:
				ans = not ans

			if ans == 0:
				result.append(1)
			else:
				result.append(2)


	answer =  np.array(result)
	final_result = (answer == test_target)

	# print test_target
	# print answer
	# print final_result
	# print final_result.mean()
	# print " "
	observations.append(final_result.mean()*100)


observations = np.array(observations)
# print observations.max()
# print observations.min()
# print observations.mean()

# print('Maximum accuracy: {0}.'.format(observations.max()))
# print('Minimum accuracy: {0}.'.format(observations.min()))
# print('Mean accuracy: {0}.'.format(observations.mean()))
best_fit_data = np.array(best_fit_data)
print best_fit_data
# print best_fit_data[0,1]
# print best_fit_data[1,0]
# print best_fit_data[1,1]
plt.scatter(best_fit_data[0,], best_fit_data[1,], marker='x', c='g')
plt.xlabel('best_t')
plt.ylabel('best_fi')
# plt.savefig(__main__.__file__+"_plot.png")
plt.show()
