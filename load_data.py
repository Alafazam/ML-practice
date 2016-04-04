from math import sqrt
import os, datetime
import time,json

from matplotlib import pyplot as plt
import numpy as np
import random

_basedir = os.path.abspath(os.path.dirname(__file__))


def loadMovieLens(path='/dataset/ml-100k'):
	# Get movie titles
	movies={}
	for line in open(_basedir + path+'/u.item'):
		(id,title)=line.split('|')[0:2]
		movies[id]=title
	print len(movies)

	# Load data
	prefs={}
	for line in open(_basedir + path+'/u.data'):
		(user,movieid,rating,ts)=line.split('\t')
		prefs.setdefault(user,{})
		prefs[user][movies[movieid]]=float(rating)

	return prefs

p = loadMovieLens()

# q = np.array(p)

print len(p)