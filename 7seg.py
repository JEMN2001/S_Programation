num = ['1111110','0110000','1101101','1111001','0110011','1011011','1011111','1110000','1111111','1111011']

def getIndex(lst,elem):
	for x in range(len(num)):
		if elem == lst[x]:
			return x
	return -1

def indices(lst, element):
    out = []
    for i in range(len(lst)):
    	if lst[i] == element:
    		out.append(i)
    return out

def getPossibles(n):
	out = []
	for i in range(10):
		tmp = []
		for j in range(n):
			tmp.append(num[(i-j)%10])
		out.append(tmp)
	return out

def redds_distance(expected,sample):
	out=[]
	for i in range(len(expected)):
		tmp1 = list(expected[i])
		tmp2 = list(sample[i])
		tmp = []
		for j in range(len(tmp1)):
			tmp.append(int(tmp1[j])-int(tmp2[j]))
		out.append(tmp)
	return out

def getLitSegments(sample):
	out = []
	for x in range(len(sample)):
		for y in range(len(sample[x])):
			if y == '1' and y not in out:
				out.append(y)
	return out

def getNext(sample):
	n = len(sample)
	poss = getPossibles(n)
	dis = []
	for i in range(10):
		dis.append(redds_distance(poss[i],sample))
	ind = []
	for i in range(len(dis)):
		det = True
		for j in range(n):
			if -1 in dis[i][j]:
				det = False
				break
		if det:
			ind.append(i)
	pos = [poss[x] for x in ind]
	dis = [dis[x] for x in ind]
	remove = []
	for x in range(len(dis)):
		litsegs = getLitSegments(pos[x])
		for y in range(len(dis[x])):
			ones = indices(dis[x][y],1)
			if len(set(ones) & set(litsegs)) > 0 and x not in remove:
				remove.append(x)
	notremoved = [x for x in range(len(dis)) if x not in remove]
	pos = [pos[x] for x in range(len(pos)) if x not in remove]
	if len(pos) == 1:
		pos=pos[0]
		dis = dis[notremoved[0]]
		damagedsegs = []
		for x in dis:
			ones = indices(x,1)
			damagedsegs += ones
		damagedsegs = list(dict.fromkeys(damagedsegs))
		out = num[(getIndex(num,pos[-1])-1)%10]
		for x in damagedsegs:
			if out[x] == '1':
				out = out[:x]+'0'+out[x+1:]
		return out
	return 'ERROR!'

file = open("A-large-practice.in",'r')
T = int(file.readline());

for i in range(T):
	tmp = []
	p = file.read(1)
	while(not p == ' '):
		tmp.append(p)
		p = file.read(1)
	size = int("".join(tmp))
	vec = []
	for j in range(size):
		vec.append(file.read(7))
		file.read(1)
	print('case#',end='')
	print(i+1,end=': ')
	print(getNext(vec))

file.close()