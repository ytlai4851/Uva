ans=[0]

for i in xrange(1,15): #k 
	m=i+1

	while True:
		k=i*2
		kill=-1
		while k>i:
			kill+=m
			kill%=k
			if kill<i:
				break
			k-=1
			kill-=1
		if k<=i:
			ans.append(m)
			break		
		m+=1
print(ans)