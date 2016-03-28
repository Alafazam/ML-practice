import __main__
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# We load the data with load_iris from sklearn
from sklearn.datasets import load_iris
data = load_iris()
features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names
labels = target_names[target]

# training = [x for x in range(0,150)]
# training.shuffle(randomz)
# training = randomz[:10]
# training = np.array(training)

# training_features = features[training]
# training_labels = labels[training]
# training_target = target[training]

# features = features[~training]
# labels = labels[~training]
# target = target[~training]




from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import KFold


classifier = KNeighborsClassifier(n_neighbors=1)

kf = KFold(len(features), n_folds=5, shuffle=True)
# `means` will be a list of mean accuracies (one entry per fold)
means = []
for training,testing in kf:
  print ("training %s",training)
  print ("testing %s",testing)
  # We fit a model for this fold, then apply it to the
  # testing data with `predict`:
  classifier.fit(features[training], labels[training])
  prediction = classifier.predict(features[testing])

  # np.mean on an array of booleans returns fraction
  # of correct decisions for this fold:
  curmean = np.mean(prediction == labels[testing])
  means.append(curmean)
print("Mean accuracy: {:.1%}".format(np.mean(means)))