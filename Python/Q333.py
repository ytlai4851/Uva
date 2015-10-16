f = open('D:\UVA\Python\Q333.txt', 'r')  
while f:
	ISBN=[]
	a=f.readline()
	a=a.rstrip('\n')
	if a=='':
		break

	for x in a:
		if x == 'X':
			ISBN.append(10)
		elif x.isdigit():
			ISBN.append(int(x))


	for i in xrange(2):
		if len(ISBN)==10:
			for x in xrange(1,10):
					ISBN[x]+=ISBN[x-1]
			if ISBN[9]%11==0:
				print("%s is correct" % a)
		else:
			print("%s isn't correct" % a)
			break