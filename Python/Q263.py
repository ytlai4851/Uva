a=raw_input()
don=1
f=-1
while don:

	b=[]
	b.extend(a.strip())
	b.sort()
	c=sorted(b,reverse=True)

	d=0
	big=0
	for i in b:
		big=big+int(i)*10**d
		d+=1
	d=0
	small=0
	for i in c:
		small=small+int(i)*10**d
		d+=1

	doneint=big-small

	print('%d-%d=%d' % (big,small,doneint))
	
	if doneint==f:
		break
	else :
		a=str(doneint)
		f=doneint



