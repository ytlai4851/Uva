b=raw_input()
a=[0,1]

for i in xrange(2,int(b)+1):
	a.append(a[i-1]+a[i-2])
	#print(a[i-1],a[i-2])
print(a.pop())
