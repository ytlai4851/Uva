a='1 2'.replace(' ','')
b=[]
for i in xrange(0,len(a),2):
	b.append(set([a[i],a[i+1]]))


for i in xrange(len(b)):
	c=[]
	try:
		for j in xrange(len(b)):
			if len(b[i]|b[j])==len(b[i])+len(b[j])-1:
				b[i] |= b[j]
				c.append(b[j])
		for j in c:
			b.pop(b.index(j))
	except Exception:
		break

if len(b)>1:
	print("no")
else:
	print('yes')