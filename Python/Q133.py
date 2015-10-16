N=13
k=17
m=42
do=0
a=[i+1 for i in range(N)]
b=a[::-1]
aindex=0
bindex=0
n=0

def kill(array,gap,index):
	x=1
	while x>-1:
		if array[index]!=0:
			x+=1
			if x > gap:
				break
		index=(index+1)%N
	return array[index]

while  n<N  :
	
	fp=kill(a,k,aindex)
	sp=kill(b,m,bindex)

	aindex=a.index(fp)
	bindex=b.index(sp)
	#print(aindex,bindex)
	if fp == sp:
		a[a.index(fp)]=0
		b[b.index(fp)]=0
		n+=1
	else:	
		a[a.index(fp)]=0
		a[a.index(sp)]=0
		b[b.index(fp)]=0	
		b[b.index(sp)]=0
		n+=2
	#print(a,b)
	print(fp,sp)