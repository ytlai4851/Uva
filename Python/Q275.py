'''a=input()
b=input()'''

a=3
b=7
quo=[]
remainder=[]
a*=10

for i in range(b):
	if a ==0 :
		print(quo,'OK')
		break
	elif a in remainder:
		z=remainder.index(a)
		print(quo,(len(quo)-z))
		break
	else :
		quo.append(a/b)
		remainder.append(a)
		a=(a%b)*10


print(quo,remainder)
