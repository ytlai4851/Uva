import collections
z=[0,0,0,0,0,0,0,0,0]

handcards=[
['AS', '2S' ,'3S' ,'4S' ,'5S'],
['AC', '2H' ,'3H' ,'5C' ,'4C'],
['AH' ,'2D' ,'KC' ,'KH' ,'5D'],
['AD' ,'3D' ,'KD' ,'9D' ,'8D'],
['XH' ,'3C' ,'XC' ,'XS' ,'8C']
]
'''
handcards=[
['2H' ,'2D' ,'3C' ,'3H' ,'3D'],
]
'''
def order(number):
	tem=[]
	re=True
	zz={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'X':10,'J':11,'Q':12,'K':13}

	for i in number:
		tem.append(zz.get(i))
	tem.sort()
	for i in xrange(4):
		if tem[i+1]-tem[i]>1:
			if tem==[1,10,11,12,13] or tem==[1,2,11,12,13]:
				break
			else:
				re=False
				break
	return re


def judgy(number,suit):
	number=collections.Counter(number)
	suit=collections.Counter(suit)
	#print(number.most_common(1))
	#print(number.most_common(1)[0][1],number.keys())
	
	if len(suit.keys())==1:
		if order(list(number.keys())):
			return 9
		else:
			return 6
	else:
		if number.most_common(1)[0][1]==4:
			return 8
		elif number.most_common(1)[0][1]==3:
			if len(number.keys())==2:
				return 7
			else:
				return 4
		elif number.most_common(1)[0][1]==2:
			if len(number.keys())==3:
				return 3
			else:
				return 2
		else:
			if order(list(number.keys())):
				return 5
			else:
				return 1


for i in handcards:
	number=[]
	suit=[]
	for x in i:
		number.append(x[0])
		suit.append(x[1])
	z[judgy(number,suit)-1]+=1

#print(z)

for x in xrange(5):
	number=[]
	suit=[]
	for j in xrange(5):
		number.append(handcards[j][x][0])
		suit.append(handcards[j][x][1])
	z[judgy(number,suit)-1]+=1
	print(number,suit,judgy(number,suit)-1)

print(z)
#print(cards)