a=raw_input()
box=a.strip().split(' ')
t=[0,0,0]
d=[]
b=[]
c=[]
cuntu=[]
bum=[0,0,0]
tc=0
for i in range(len(box)):
	box[i]=int(box[i])
	if i<3:
		t[0]+=box[i]
		d.append(box[i])
	elif i<6 :
		t[1]+=box[i]
		b.append(box[i])
	else :
		t[2]+=box[i]
		c.append(box[i])

def big(org):
	tem=org[:]
	bigsort=sorted(tem,reverse=True)
	for i in range(3):
		bigsort[i]=tem.index(bigsort[i])
		tem[bigsort[i]]=-1
	for i in bigsort:
		if i not in cuntu:
			z=i
			break
	cuntu.append(z)
	return z


	
	
ts=sorted(t,reverse=True)
for i in range(3):
	ts[i]=t.index(ts[i])

print(d,b,c,ts)

for i in ts:
	if i==0:
		bum[i]=(big(d))
		d[bum[i]]=0
		print(d)
	elif i ==1:
		bum[i]=(big(b))
		b[bum[i]]=0
	else :
		bum[i]=(big(c))
		c[bum[i]]=0
for i in range(3):
	tc+=d[i]+c[i]+b[i]
	print(d[i],c[i],b[i])
print(bum,d,b,c,tc)