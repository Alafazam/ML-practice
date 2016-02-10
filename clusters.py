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




def hcluster(rows, distance = pearson):
	distances =  {}
	currentclustid = -1

	#clusters are initially just the row
	clust = [bicluster(rows[i],id=i) for i in range(len(rows))]

	while len(clust) > 2:
		lowestpair = (0,1)
		closest = distance(clust[0].vec,clust[1].vec)

		#loop through every pair looking for smallest distance
		for i in range(len(clust)):
			for j in range(i+1, len(clust)):
				# distance is the cache of distance calulations
				if(clust[i].id, clust[j].id) not in distances:
					distances[(clust[i].id, clust[j].id)] = distance(clust[i].vec,clust[j].vec)

				d = distances[(clust[i].id,clust[j].id)]

				if d < closest:
					closest = d
					lowestpair = (i,j)
		# calulate the average of two clusters

		mergevec =  [ (clust[lowestpair[0]].vec[i] + clust[lowestpair[1]].vec[i])/2.0 for i in range(len(clust[0].vec))]

		#create the new cluster
		newcluster= bicluster(mergevec,left=clust[lowestpair[0]], right=clust[lowestpair[1]],distance=closest,id=currentclustid)

		# cluster ids that weren't in the original set are negative
		currentclustid-=1
		del clust[lowestpair[1]]
		del clust[lowestpair[0]]
		clust.append(newcluster)

	return clust[0]

