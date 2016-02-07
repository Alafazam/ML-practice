from recommendations import critics
from sim_dist import *



t = sim_distance(critics,'Lisa Rose','Gene Seymour')
q = sim_pearson(critics,'Lisa Rose','Gene Seymour')

# print "distance:"
# print t

# print "preason coeff"
# print q
# print ""

scores = topMatches(critics, 'Toby')
print "scores:" , scores
print ""

# recommendation = getRecommendations(critics,'Toby')
# print recommendation
# print ""


movies = transformPrefs(critics)
# print "movies:", movies
# print ""


scores2 = topMatches(movies,'Superman Returns')
print "TopMatches in movies of 'Superman Returns' ", scores2
print ""

#similarity list
itemsim = calculateSimilarItems(critics)
print "SimilarItems: ", itemsim



# see what user likes, take each items similarity list 
#  	 to get most similar unrated item
recom = getRecommendedItems(critics, itemsim, 'Toby')
print "RecommendedItems", recom
