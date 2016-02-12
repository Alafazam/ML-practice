from clusters import *
from pearson_corelation2 import *


blognames,words,data = readfile('blogdata.txt')


# # print len(data)


clust = hcluster(data)

# # clust = [bicluster(data[i],id=i) for i in range(len(data))]

# # printClust(clust, labels=blognames)


# print "writeClust"



# writeClust(clust, labels=blognames)

drawdendrogram(clust,blognames,jpeg='blogclust.jpg')



