from sim_dist import *



ds = loadMovieLens()
print "data set loaded"


# select a random user
print ds['100']


recommendation_for_user = getRecommendations(ds,'100')[0:30]
print "recommendation user based:\n", recommendation_for_user




itemsim = calculateSimilarItems(ds,n=50)


recommend_from_items = getRecommendedItems(ds,itemsim,'100')[0:30]
print "recommend items based:\n", recommendation_for_user
