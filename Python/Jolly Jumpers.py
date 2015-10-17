a = raw_input()
b=[]
c1=[]
d=bool

a=a.strip().split(' ')
for i in range(len(a)):
	b.append(int(a[i]))

for i in range(len(b)-1):
	c1.append(abs(b[i+1]-b[i]))

	if i>0:
		d=c1[i]+1==c1[i-1]
		if d!=1:
			break
if d:
	print("jolly")
else :
	print("no")
