a=raw_input()

while a:
	if a =='0 0':
		break
	a=a.strip().split(' ')
	b=1
	c=1
	for x in xrange(1,int(a[1])+1):
		b*=(int(a[0])-x+1)
		c*=x
	print("%s things taken %s at a time is %d exactly" % (a[0],a[1],b/c))
	a=raw_input()
