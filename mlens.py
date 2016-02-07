from sim_dist import *



ds = loadMovieLens()
print "data set loaded"


# select a random user
print ds['100']


recommendation_for_user = getRecommendations(ds,'100')[0:30]
print "recommendation for user :\n", recommendation_for_user