def mean(seq,pro,sort=True,top=0):
	if top == 0: top = len(seq)

	seq = sorted(seq, key=lambda x: x[pro], reverse=True)

	m = 0
	for xz in range(top):
		m += seq[xz][pro]
	return m/top



def median(seq,pro):
	med = 0
	seq = sorted(seq, key=lambda x: x[pro], reverse=True)
	mid = int(len(seq)/2)
	return seq[mid][pro]

def mode(seq,pro):
	pass