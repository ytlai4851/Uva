a=input()
b=[x for x in range(0,a+1)]
k=input()
area=0
tem=0

while a>1:
	z=0
	while z<1:
		tem+=k
		if tem >len(b)-1:
			tem=0
		if b[tem]>0:
			z+=1

	print(tem)
	b[tem]=0
	print(b)
	tem1=tem
	print(tem1)

	while z<1:
		tem1+=k
		print(tem1)
		if tem1 >a:
			tem1=0
		elif b[tem1]>0:
			z+=1
	
	print(tem1,tem)
	b[tem]=b[tem1]
	b[tem1]=0


	a-=1