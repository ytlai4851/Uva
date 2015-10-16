test='ED'

b=max(test)

try:
	b=int(b)
except ValueError:
	b=ord(b)-55

x=15

def add(num1,num2,base):
	num=0
	for x in xrange(len(num1),0,-1):
		try:
			num+=int(num1[x-1])*(base**(len(num1)-x))
		except ValueError:
			num+=(ord(num1[x-1])-55)*(base**(len(num1)-x))
		try:
			num+=int(num2[x-1])*(base**(len(num1)-x))
		except ValueError:
			num+=(ord(num2[x-1])-55)*(base**(len(num1)-x))
	reslut_tra=''

 	while num>=base:
 		if num%base>9:
 			reslut_tra=chr((num%base)+55)+reslut_tra
 		else:
 			reslut_tra=str(num%base)+reslut_tra
 		num=num/base
 	if num>9:
 		reslut_tra=chr(num+55)+reslut_tra
 	else:
 		reslut_tra=str(num)+reslut_tra
 	return(reslut_tra)

for x in xrange(15,1,-1):
	a=test
	count=0
	if x > b:
		while a !=a[::-1]:
			a=add(a,a[::-1],x)
			count+=1
		if count>0:
			print(count)
	else:
		print('?')



