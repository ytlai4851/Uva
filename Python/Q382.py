a=60000
b=[]
for i in range(1,a):
	if a % i ==0:
		b.append(i)


c=sum(b)
print(b,c)
if c==a:
	print('perfect')
elif c>a :
	print('a')
else :
	print('d')
