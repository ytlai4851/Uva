previous=[]

def big_add(a):
	max_length=len(max(a,key=len))
	tem=0
	carry=0

	for i in xrange(len(a)):
		while len(a[i])<max_length:
			a[i]='0'+a[i]

	for x in xrange(len(a)):
		a[x]=a[x][::-1]
	out=''

	for x in xrange(max_length):
		for i in a:
			tem+=int(i[x])
		tem+=carry
		carry=0
		if tem>9:
			carry=tem/10
		out=str(tem%10)+out
		tem=0

	if carry > 0:
		out=str(carry)+out
	return out 


#print(big_add(['7','12']))
x=1

while True:
	if str(10**60) in previous:
		break
	x+=1
	now=['1']
	for j in xrange(1,x):
		pp=[]
		try:
			pp.append(previous[j-1])
			pp.append(previous[j])
			now.append(big_add(pp))
		except :
			pass
	if x > 1 :
		now.append('1')
	previous=now
print(now)
