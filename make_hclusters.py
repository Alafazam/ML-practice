from clusters import *
from pearson_corelation2 import *


blognames,words,data = readfile('blogdata.txt')

# clust = hcluster(data)

print len(data)


clust = [bicluster(data[i],id=i) for i in range(len(data))]

print  clust[0]



