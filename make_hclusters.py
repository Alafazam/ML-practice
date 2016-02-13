from clusters import *
from pearson_corelation2 import *


blognames,words,data = readfile('blogdata.txt')


# # print len(data)


clust = hcluster(data)
drawdendrogram(clust,blognames,jpeg='blogclust.jpg')


rdata = rotatematrix(data)

wordclust=hcluster(rdata)

drawdendrogram(wordclust,labels=words,jpeg='wordclust.jpg')