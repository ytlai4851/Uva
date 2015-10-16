a="azyxwvutsrqpppooonnnmmmlllkkkjjjiiihhhgfedcccbbaaa"
b=[]



def organize(alp):
	b.append(alp)
	b.sort()
	tem=''
	if max(b)>alp :
		for i in b:
			if i >alp:
				tem=b.pop(b.index(i))
				tem=tem+''.join(str(e) for e in b)
				#print(tem1,tem))
				break
		return(tem)



		



for x in xrange(len(a),0,-1):
	#print(a[x-1])
	z=organize(a[x-1])
	a=a[0:len(a)-1]
	if z!=None:
		z=a+z
		print(z)
		break
if z==None:
	print("No")
elif z =="baaaabcccdefghhhiiijjjkkklllmmmnnnooopppqrstuvwxyz":
	print("T")


'''

for x in xrange(len(a)-1):
	if a[len(a)-1]>b[0]:
		b=a[len(a)-1]+b
		a=a[0:len(a)-1]
		break
	elif x==len(a)-2:
		print("no")
print(a,b)
		
'''
