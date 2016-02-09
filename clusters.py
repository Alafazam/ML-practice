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