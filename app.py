from recommendations import critics
from sim_dist import *



t = sim_distance(critics,'Lisa Rose','Gene Seymour')
q = sim_pearson(critics,'Lisa Rose','Gene Seymour')

print "distance:"
print t

print "preason coeff"
print q
print ""

scores = topMatches(critics, 'Toby', n=3)
print scores
print ""


recommendation = getRecommendations(critics,'Toby')
print recommendation
print ""


movies = transformPrefs(critics)
print movies
print ""


scores2 = topMatches(movies,'Superman Returns')
print scores2
print ""


itemsim=calculateSimilarItems(critics)
print itemsim