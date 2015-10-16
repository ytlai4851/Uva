
#a=['dip','lip','mad','map','may','pad','pip','pod','pop','sap','sip']
a=['slice','slick','spice','stick','stock']
visited=[]

#b='may'
#c='pod'
b='spice'
c='stock'


def differnet(str1 , str2):
	count=0
	for x in xrange( len(str1)):
		if str1[x] != str2[x]:
			count+=1
	return count


def next(now,count):
	tem=[]
	print(visited)
	for i in now:
		for x in a :
			if x not in visited:
				if differnet(i,x) ==1:
					visited.append(x)
					print(i,x)
					tem.append(x)
	if c not in visited:
		return next(tem,count+1)
	print(count)

next([b],1)

