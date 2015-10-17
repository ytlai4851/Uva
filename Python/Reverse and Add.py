a= raw_input()
z=0
cout=0
while z==0:
	b=int(a,10)
	c=int(a[::-1])
	tem=b+c
	a=str(tem)
	cout+=1
	if(b==c):
		z=1
		break
print(b,c,cout-1)