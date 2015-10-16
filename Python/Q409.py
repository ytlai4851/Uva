import string
delete_table  = string.maketrans(string.ascii_lowercase, ' ' * len(string.ascii_lowercase))
K=6
E=5
excuse=[]
excuse_count=0
max_s=[]
f=open('D:\UVA\Python\Q409.txt','r')

for i in xrange(K):
	excuse.append(f.readline().rstrip('\n'))
#print(excuse)

for i in xrange(E):
	temc=0
	s=f.readline().rstrip('\n').strip().split(' ')
	#print(s)
	for x in s:
		x=x.lower()
		if x.translate(None,delete_table) in excuse:
	#		print(x)
			temc+=1
	if temc>excuse_count:
		excuse_count=temc
		max_s=[]
		max_s.append(s)
	elif temc==excuse_count:
		max_s.append(s)
print(max_s,excuse_count)

