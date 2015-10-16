import pdb

a='1355'
a=a.strip()
b=raw_input()
b=b.strip()



gameover='0'
for x in range(0,len(a)-1):
	gameover+='0'

while b!=gameover:
	A=0
	B=0
	adonenum=[1 for i in range(len(a))]
	bdonenum=[1 for i in range(len(b))]	
	for i in range(0,len(b)):
		if b[i]==a[i]:
			A+=1
			adonenum[i]=0
			bdonenum[i]=0


	for i in range(0,len(b)):
		if bdonenum[i]!=0:
			for j in range(0,len(a)):
				if b[i]==a[j] and adonenum[j]!=0:
					B+=1
					adonenum[j]=0
					bdonenum[i]=0


	print(A,B)
	b=raw_input()
	b=b.strip()


