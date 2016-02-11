from pearson_corelation2 import *
from cluster import *


def readfile(filename):
	lines = [line for line in file(filename)]
	#First line is column titles
	colnames = lines[0].strip().split('\t')[1:]
	rownames = []
	data = []
	for line in lines[1:]:
		p = line.strip().split('\t')
		# first col is blog name
		rownames.append(p[0])
		# the data for this row is remaineder of the row
		data.append([float(x) for x in p[1:]])
	return rownames,colnames,data


def hcluster(rows,distance=pearson):
	distances={}
	currentclustid=-1
	# Clusters are initially just the rows
	clust=[bicluster(rows[i],id=i) for i in range(len(rows))]
	
	while len(clust)>1:
		lowestpair=(0,1)
		closest=distance(clust[0].vec,clust[1].vec)
		# loop through every pair looking for the smallest distance
		for i in range(len(clust)):
			for j in range(i+1,len(clust)):
			# distances is the cache of distance calculations
				if (clust[i].id,clust[j].id) not in distances:
					distances[(clust[i].id,clust[j].id)]=distance(clust[i].vec,clust[j].vec)
					
				d=distances[(clust[i].id,clust[j].id)]
				
				if d<closest:
					closest=d
					lowestpair=(i,j)
		
		minL = min(len(clust[lowestpair[0]].vec),len(clust[lowestpair[1]].vec))
		# calculate the average of the two clusters
		mergevec=[(clust[lowestpair[0]].vec[i] + clust[lowestpair[1]].vec[i])/2.0 for i in range(minL)]
		# create the new cluster
		newcluster=bicluster(mergevec,left=clust[lowestpair[0]], right=clust[lowestpair[1]], distance=closest,id=currentclustid)
		# cluster ids that weren't in the original set are negative
		currentclustid-=1
		del clust[lowestpair[1]]
		del clust[lowestpair[0]]
		clust.append(newcluster)


	return clust[0]





def printClust(clust, labels=None, n=0):
	#indent to make hierarch layout
	for i in range(n): print ' ',
	if clust.id<0:
		#negative id means this is branch
		print '____'
	else:
		# positive id means this is an endpoint
		if labels==None: print clust.id
		else: print labels[clust.id]
	# now print the right and left branches
	if clust.left!=None: printClust(clust.left,labels=labels,n=n+1)
	if clust.right!=None: printClust(clust.right,labels=labels,n=n+1)


def writeClust(clust, labels=None, n=0):
	print 'now writing clusters to cluster.txt '
	out = file('cluster.txt','w')
	out.write('sdadasdsa')
	#indent to make hierarch layout
	for i in range(n): out.write(' '),
	if clust.id<0:
		#negative id means this is branch
		out.write('____')
	else:
		# positive id means this is an endpoint
		if labels==None: out.write(clust.id)
		else: out.write(str(labels[clust.id]))
	# out.write('\n')	
	# now print the right and left branches
	if clust.left!=None: printClust(clust.left,labels=labels,n=n+1)
	if clust.right!=None: printClust(clust.right,labels=labels,n=n+1)

