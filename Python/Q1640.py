a=1001
b=1960
count=[0 for i in xrange(10)]

for i in xrange(a,b+1):
	for j in str(i):
		#print(j)
		count[int(j)]+=1
print(count)