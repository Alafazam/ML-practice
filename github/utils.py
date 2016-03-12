def mean(seq,pro,sort=True,top=0):
	if top == 0: top = len(seq)

	seq = sorted(seq, key=lambda x: x[pro], reverse=True)

	m = 0
	for xz in range(top):
		m += seq[xz][pro]
	return m/top



def median(seq,pro,top=0):
	if top == 0: top = len(seq)
	med = 0
	seq = sorted(seq, key=lambda x: x[pro], reverse=True)[:top]
	mid = int(top/2)
	return seq[mid][pro]

def mode(seq,pro,top=0):
	return 3*median(seq,pro,top) - 2*mean(seq,pro,top)