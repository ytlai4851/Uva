c='0'

recodearea=[i for i in range(10)]
list1=[]
tem=[]

for i in range(10):
	tem=[]
	tem.append(str(i))
	list1.extend([tem])

def movetop(boxnum):
	z=list1[recodearea[boxnum]].index(str(boxnum))
	for i in range(len(list1[recodearea[boxnum]])-1,z,-1):
		recodearea[int(list1[recodearea[boxnum]][i])]=int(list1[recodearea[boxnum]][i])
		list1[int(list1[recodearea[boxnum]][i])]=[list1[recodearea[boxnum]][i]]
		list1[recodearea[boxnum]].remove(list1[recodearea[boxnum]][i])

def moveall(boxnum):
	z=list1[recodearea[boxnum]].index(str(boxnum))
	for i in range(z,len(list1[recodearea[boxnum]])-1):
		recodearea[int(list1[recodearea[boxnum]][i])]=int(list1[recodearea[boxnum]][i])
		list1[int(list1[recodearea[boxnum]][i])]=[list1[recodearea[boxnum]][i]]

def mon(a,b):
	movetop(a)
	movetop(b)
	list1[recodearea[b]].extend(str(a))
	list1[recodearea[a]].remove(str(a))
	recodearea[a]=recodearea[b]

def moo(a,b):
	movetop(a)
	list1[recodearea[b]].extend(str(a))
	list1[recodearea[a]].remove(str(a))
	recodearea[a]=recodearea[b]

def pio(a,b):
	movetop(b)
	z=list1[recodearea[a]].index(str(a))
	for i in range(z,len(list1[recodearea[a]])-1):
		print(recodearea[b])
		list1[3].extend('6')
		list1[recodearea[b]].append('5')
		list1[recodearea[b]].remove(list1[recodearea[a]][i])
		recodearea[int(list1[recodearea[a]][i])]=recodearea[b]

while c!= 'q':
	c=raw_input()
	a=input()
	b=input()
	
	if c=='1':
		mon(a,b)
	elif c=='2' :
		moo(a,b)
	elif c =='3':
		pio(a,b)

	print(recodearea)
	print(list1)