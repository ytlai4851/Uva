# -*- coding: utf-8 -*- 
al=[]
a=['xwy','zx','zxy','zxw','ywwx']

for i in xrange(len(a)):
	for x in a[i]:
		if x not in al:
			al.extend(x)
b=[[] for x in xrange(len(al))]  #字母


for i in xrange(len(a)-1):
	if len(a[i])==len(a[i+1]):
		for x in xrange(len(a[i])):
			if a[i][x]!=a[i+1][x]:
				b[al.index(a[i+1][x])].append(a[i][x])
	else :
		if a[i][0] not in b[al.index(a[i+1][0])] and a[i][0]!=a[i+1][0] :
			b[al.index(a[i+1][0])].append(a[i][0])
	print(a[i])
out=''

x=0
while x !=-1:
	if len(b)==0 :
		break
	elif b[x] ==[]:
		out+=al[x]
		print(b)
		for i in xrange(len(b)):
			if al[x] in b[i]:
				b[i].pop(b[i].index(al[x]))
		al.pop(x)
		b.pop(x)
		x=0
	else:
		x+=1
	print(out)

