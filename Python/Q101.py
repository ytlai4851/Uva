c='0'

recodearea=[i for i in range(10)]
list1=[str(i) for i in range(10)]


def splitz(boxtop):
	boxtop.strip()
	return boxtop

def movetop(boxnum):
	boxtop=[]
	boxtop.extend(splitz(list1[recodearea[boxnum]]))

	for i in range(boxtop.index(str(boxnum))+1,len(boxtop)):
		list1[int(boxtop[i])]=boxtop[i]
		recodearea[int(boxtop[i])]=int(boxtop[i])


		

def mon(a,b):
	movetop(a)
	movetop(b)
	if list1[a]!=None:
		list1[recodearea[b]]+=str(a)
		list1[a]=None
		recodearea[int(a)]=recodearea[b]


def moo(a,b):
	movetop(b)




while c!= 'q':
	c=raw_input()
	a=input()
	b=input()
	
	if c=='1':
		mon(a,b)
	elif c=='2' :
		moo(a,b)

	print(recodearea)
	print(list1)
