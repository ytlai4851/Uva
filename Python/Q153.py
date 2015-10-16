gg="bacaa"


original=list(gg)
original.sort()
b=[]
a=''.join(original)
c=a[::-1]
out=[]
y=len(a)-1
c=1

def organize(alp):
	b.append(alp)
	b.sort()
	tem=''
	if max(b)>alp :
		for i in b:
			if i >alp:
				tem=b.pop(b.index(i))
				tem=tem+''.join(str(e) for e in b)
				break
		#print(tem)
		return(tem)

while y>=0:
	z=""
	z=organize(a[y])
	a=a[0:y]

	if z!=None:
		print(a,z)
		z=a+z
		out.append(z)
		a=z
		print(a)
		y=len(a)-1
		b=[]
	else:
		y-=1
print(out.index(gg)+2)