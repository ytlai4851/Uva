a='1234567'
c=[]
i=0

while True:
	i+=1
	b=int(a)*i
	if b >= 10000000000:
		break
	zz=set(str(b))
	if len(zz)==len(str(b)):
		print(b,i)
		
