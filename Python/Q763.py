fin=[1,2]

for i in xrange(100):
	a , b = fin[-1],fin[-2]
	fin.append(a+b)

def Translate_Base10(num):
	tema=0
	for i in xrange(len(num)):
		tema+=int(num[i])*fin[i]
	return tema
def Translate_Fib(num):
	Fib_S=''
	i=0
	while fin[i]<=num:
		i+=1
	for j in xrange(i-1,0,-1):
		if fin[j]<=num:
			num-=fin[j]
			Fib_S+='1'
		else:
			Fib_S+='0'
	if num:
		Fib_S+='1'
	else:
		Fib_S+='0'
	return Fib_S

a='10010'[::-1]
b='1'[::-1]

print(Translate_Fib( Translate_Base10(a)+Translate_Base10(b)))