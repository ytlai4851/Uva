a=[i for i in range(1,48)]
b=6
y=[11,2,7,3,4,8,5,10,7,8,3,7,4,2,3,9,10,2,5,3]

to=max(a)-b
print(a)
while len(a)>b:
	z=0
	c=y[0]
	while z+c <=len(a):
		if to >0:
			a[z+c-1]=0
			to-=1
		z+=c
	a=filter(lambda x :x>0,a)
 	y.remove(c)	
	print(a,c)

