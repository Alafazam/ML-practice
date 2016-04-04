from pearson_corelation2 import *
from cluster import *
from PIL import Image,ImageDraw
import random

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



def rotatematrix(data):
	newdata=[]
	for i in range(len(data[0])):
		newrow=[data[j][i] for j in range(len(data))]
		newdata.append(newrow)
	return newdata


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

def getheight(clust):
	#is this an endpoint, then hieght is just 1
	if clust.left==None and clust.right == None: return 1

	#otherwise the height is the same of the heights of each branch
	return getheight(clust.left) + getheight(clust.right)


def getdepth(clust):
	# the distance of and endpoint is 0.0
	if clust.left == None and clust.right == None : return 1
	return max(getdepth(clust.left),getdepth(clust.right))+clust.distance







def drawdendrogram(clust,labels,jpeg='clusters.jpg'):
	# height and width
	h = getheight(clust)*20
	w = 1200
	depth = getdepth(clust)
	# width is fixed, so scale distances accordingly
	scaling = float(w-150)/depth
	# Create a new image with a white background
	img = Image.new('RGB',(w,h),(255,255,255))
	draw = ImageDraw.Draw(img)
	draw.line((0,h/2,10,h/2),fill=(255,0,0))
	# Draw the first node
	drawnode(draw,clust,10,(h/2),scaling,labels)
	img.save(jpeg,'JPEG')



def drawnode(draw,clust,x,y,scaling,labels):
	if clust.id<0:
		h1=getheight(clust.left)*20
		h2=getheight(clust.right)*20
		top=y-(h1+h2)/2
		bottom=y+(h1+h2)/2
		# Line length
		ll=clust.distance*scaling
		# Vertical line from this cluster to children
		draw.line((x,top+h1/2,x,bottom-h2/2),fill=(255,0,0))
		# Horizontal line to left item
		draw.line((x,top+h1/2,x+ll,top+h1/2),fill=(255,0,0))
		# Horizontal line to right item
		draw.line((x,bottom-h2/2,x+ll,bottom-h2/2),fill=(255,0,0))
		# Call the function to draw the left and right nodes
		drawnode(draw,clust.left,x+ll,top+h1/2,scaling,labels)
		drawnode(draw,clust.right,x+ll,bottom-h2/2,scaling,labels)
	else:
		# If this is an endpoint, draw the item label
		draw.text((x+5,y-7),labels[clust.id],(0,0,0))






def kcluster(rows,distance=pearson,k=4):
	# Determine the minimum and maximum values for each point
	rows = rows[1:]
	ranges = [ (min([row[i] for row in rows]), max([row[i] for row in rows])) for i in range(len(rows[0]))]
	# print 'ranges',ranges
	# Create k randomly placed centroids
	clusters = [[random.random( )*(ranges[i][1]-ranges[i][0])+ranges[i][0] for i in range(len(rows[0]))] for j in range(k)]	
	lastmatches=None
	for t in range(100):
		# print 'Iteration %d' % t
		bestmatches=[[] for i in range(k)]
		# Find which centroid is the closest for each row
		for j in range(len(rows)):
			row = rows[j]
			bestmatch = 0
			for i in range(k):
				d = distance(clusters[i],row)
				if d < distance(clusters[bestmatch],row): bestmatch = i
			bestmatches[bestmatch].append(j)
			# If the results are the same as last time, this is complete
		if bestmatches == lastmatches: break
		lastmatches = bestmatches
		#Move the centroids to the average of their members
		for i in range(k):
			avgs=[0.0]*len(rows[1])
			if len(bestmatches[i])>0:
				for rowid in bestmatches[i]:
					for m in range(len(rows[rowid])):
						avgs[m]+=rows[rowid][m]
				for j in range(len(avgs)):
					avgs[j]/=len(bestmatches[i])
				clusters[i]=avgs
	return bestmatches