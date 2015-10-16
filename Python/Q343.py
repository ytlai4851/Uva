import pdb
z='10'
x='A'
a=[]
b=[]
for i in z:
	try:
		a.append(int(i))
	except ValueError :
		a.append(ord(a[j-1])-55)


allofa=[0 for i in range(37)]


for i in range(int(max(a))+1,37):
	anum=0
	for j in range(len(a),0,-1):
		try:
			anum+=(i**(len(a)-j))*int(a[j-1])
		except ValueError:
			anum+=(i**(len(a)-j))*(ord(a[j-1])-55)
	allofa[i]=anum


for i in range(int(max(b))+1,37):
	bnum=0
	for j in range(len(b),0,-1):
		try:
			bnum+=(i**(len(b)-j))*int(b[j-1])
		except ValueError:
			bnum+=(i**(len(b)-j))*(ord(b[j-1])-55)
	allofa[i]=anum
	if bnum in allofa :
		print(allofa.index(bnum),i)
		break
	
	print('Z')



