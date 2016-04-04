from math import sqrt

def pearson(v1,v2):
	# simple sums

	sum1 = sum(v1)
	sum2 = sum(v2)

	#sum of squares
	sumSq1 = sum([pow(v,2) for v in v1])
	sumSq2 = sum([pow(v,2) for v in v2])

	minLen = len(v1)
	if len(v2) < minLen:
		minLen = len(v2)

 	#sum of the products
	pSum = sum([v1[i] * v2[i] for i in range(minLen)])

	#pearson score r
	num = pSum - (sum1*sum2/len(v1))
	den = sqrt( (sumSq1-pow(sum1,2)/len(v1))*(sumSq2-pow(sum2,2)/len(v2)))
	if den==0: return 0

	return 1.0-num/den