a=input()
b=input()
c=[]
d=[]

def zz (a):
	x=[]
	while a!=0:
		x.insert(0,a%10)
		a=a/10
	return x

def yy(a,b):
	count=0
	pp=0
	for i in range(ff-1,-1,-1):
		a[i]=a[i]+pp
		pp=0
		if a[i]+b[i]>=10:
		 	count+=1 
		 	pp+=1
		#print(i)
	return count

c=zz(a)
d=zz(b)

if len(c)>len(d):
	ff=len(c)-len(d)
	for i in range(ff):
		d.insert(0,0)
	ff=len(c)
elif len(c)<len(d):
	ff=len(d)-len(c)
	for i in range(ff):
		c.insert(0,0)
	ff=len(d)
else :
	ff=len(c)
#print(ff)
gg=yy(c,d)
if gg>1:
	print('%d s'%(gg))
else:
	print('%d'%(gg))



