#c=['AB','CE','DB','EC']
c=['AB']
a=[set()]
zz=['A','B','C','D','E']

def add(b,c):
	try :
		zz.pop(zz.index(b))
		zz.pop(zz.index(c))
	except:
		pass
	tem=set()
	for i in xrange (len(a)):
		if b in a[i] or c in a[i]:
			a[i].update(b,c)
			return 
	
	tem.update(b,c)
	a.append(tem)

for x in c:
	add(x[0],x[1])
print(len(a)-1+len(zz))