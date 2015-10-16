b=[i for i in range(2,600)]
for i in (b):
	for j in range(i,600):
		try:
			b.remove(i*j)
		except ValueError:
			pass

def primefactor(n):
	primecount=1
	for i in (b):
		count=1
		if i<=n:
			while n%i==0:
				n/=i
				count+=1
		else:
			break
		primecount=primecount*count
	return primecount

			

totalfactor=[[None],[None]]
#totalfactor[1].append(primefactor(6))

a=999999924
c=1000000000
for i in range(a,c+1):
	if i not in b:
		totalfactor[0].append(i)
		totalfactor[1].append(primefactor(i))
#print(totalfactor)
print(totalfactor[0] [totalfactor[1].index( max(totalfactor[1]))],max(totalfactor[1]))
