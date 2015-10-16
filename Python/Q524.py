prime=[2,3,5,7,11,13,17,19,23,29,31,37,41]
a=[1,2,3,4,5,6,7,8]
cycle=['1']

for x in cycle:
	for i in xrange(2,len(a)+1):
		if int(x[-1]) + i in prime and str(i) not in x:
			cycle.append(x+str(i))
for x in cycle:
	if  len(x) == len(a) and int(x[0])+int(x[-1]) in prime :
		print(x) 
