from recommendations import critics
from sim_dist import *



t = sim_distance(critics,'Lisa Rose','Gene Seymour')
q = sim_pearson(critics,'Lisa Rose','Gene Seymour')

print "distance:"
print t

print "preason coeff"
print q
