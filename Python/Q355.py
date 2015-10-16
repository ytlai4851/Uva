a=5
b=3
c='126'
turn10=0
num=[]
todo=1
for i in c:
	try:
		if int(i)<a:
			num.append(int(i))
		else:
			todo=0
			break
	except ValueError:
		if ord(i)-55 <a :
			num.append(ord(i)-55)
		else:
			todo=0
			break

if todo:
	z=0
	for i in range(len(num),0,-1):

		turn10+=num[i-1]*(a**z)
		print(turn10,a**z)
		z+=1

	num=[]


	while turn10 >b:
		num.append(turn10%b)
		turn10//=b
	num.append(turn10)
	num.reverse()
	print(num)
else:
	print('No')