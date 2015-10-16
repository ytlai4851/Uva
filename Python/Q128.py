a= 'this is a test'
g=34943
c=[]

for i in a:
	c.append(ord(i))

for x in range(len(c)):
	c[x]=c[x]*(256**(len(c)+1-x))
n=sum(c)
print(n)
x=hex(g-(n%g))[2:-1]
print(x)
