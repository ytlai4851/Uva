a=input()
b=[]
z=1
while len(b)<a:
	c=z
	for i in range(c):
		if z%2==0:
			b.append(str(i+1)+'/'+str(c))
		else:
			b.append(str(c)+'/'+str(i+1))
		c-=1
	z+=1
	

print(b[a-1])