a = input()
b=[i for i in range(2,100+1)]

for i in (b):
	for j in range(2,((len(b)+1)/2)+1):
		try:
			b.remove(i*j)
		except ValueError:
			pass

c=[0 for i in range(len(b))]

'''
def prime(z):
	for i in b:
		if z%i ==0:
			c[b.index(i)]+=1
			z=z/i



	if i in b:
		c[b.index(i)]+=1
		print(i,c)
	else:
		prime(i)

'''
for z in range(2,a+1):
	for i in b:
		if  z in b:
			c[b.index(z)]+=1
			break
		else:
			while z%i ==0:
				c[b.index(i)]+=1
				z=z/i
print(c)

for i in c:
	if i==0:
		c.remove(i)
print(c)