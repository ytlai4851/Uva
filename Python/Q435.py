import itertools

possible=set()
party={'1':12,'2':9,'3':7,'4':3,'5':1,'6':1}
half=(sum(party.values())+1)/2

power=[0 for i in xrange(len(party.keys()))]

possible=[]


for i in xrange(1,len(party)):
	for x in  list(itertools.combinations(list(party.keys()),i)):
		possible.append(x)


for j in xrange(1,len(party.keys())+1):
	for x in possible:
		tem=0
		if str(j) not in x:
			for i in x:
				tem+=party.get(i)
		if  tem<half and tem+party.get(str(j)) >= half:
			power[j-1]+=1
#			print(x,j)
print(power)

#print(possible)