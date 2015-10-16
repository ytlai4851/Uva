a='KKKKKKKKKKKKKKKKKKKKKKKKKKK'

for i in xrange(1,len(a)+1):
	b=a[:i]
	if a.count(b)*len(b) == len(a):
		print(len(b))
		break

