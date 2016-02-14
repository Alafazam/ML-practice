from clusters import *
from pearson_corelation2 import *


blognames,words,data = readfile('blogdata.txt')


# arr =  [len(data[x]) for x in range(len(data))]
# print arr


# clust = hcluster(data)
# drawdendrogram(clust,blognames,jpeg='blogclust.jpg')


# rdata = rotatematrix(data)

# wordclust=hcluster(rdata)

# drawdendrogram(wordclust,labels=words,jpeg='wordclust.jpg'


kclust = kcluster(data,k=10)


