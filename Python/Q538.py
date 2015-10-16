N = 46340
table = list(range(N))
for i in range(2,int(N**0.5)+1):
    if table[i]:
        for mult in range(i**2,N,i):
            table[mult] = False
 
primetable= [p for p in table if p][1:]

p=0
a=196
if a<0:
	p=1
	a*=-1
b=''

while True:
	if a in primetable:
		b+=str(a)
		break
	for i in primetable:
		if a % i ==0:
			a=a/i
			b+=str(i)+' x '
			break
if p :
	b='-1 x '+b
print(b)




