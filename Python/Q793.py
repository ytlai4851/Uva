f=open('I:\\Coding Practice\\UVA\\Python\\Q793.txt','r')
Connection=[0 for i in xrange(int(f.readline())+1)]

def Join_To_Same(a,b):
	for i in xrange(len(Connection)):
		if Connection[i]==a or Connection[i]==b:
			Connection[i]=a
fail=0
s=0
while True:
	a=f.readline().replace(' ','')
	if a == '':
		break
	Node1=int(a[1])
	Node2=int(a[2])
	if a[0] == 'c':
		if Connection[Node1]==0 and Connection[Node2]==0:
			Connection[Node1],Connection[Node2]=Node1,Node1
		elif Connection[Node1]==0 :
			Connection[Node1]=Connection[Node2]
		elif Connection[Node2]==0 :
			Connection[Node2]=Connection[Node1]
		else:
			Join_To_Same(Connection[Node1],Connection[Node2])
	else:
		if Connection[Node1]!=Connection[Node2]:
			fail+=1
		else:
			s+=1
			
print(s,fail)