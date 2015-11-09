a=[0]
n=1000000
for i in xrange(2,n+1):
	tem,totle,j=i,0,2
	while j<=int(tem**0.5)+1:
		while tem%j==0:
			tem/=j
			totle+=1
			if tem<j:
				break
		j+=1
	if tem!=1:
		totle+=1
	a.append(totle+a[-1])
print(a[-1])