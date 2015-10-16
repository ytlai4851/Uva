a=input()
if a==2:
	for i in range(100):
		if i<10:
			z=('0'+str(i))
			z=str((int(z[:a/2])+int(z[a/2:]))**2)
			if int(z)==i:
				print('0'+z)
		else :
			z=str(i)
			z=str((int(z[:a/2])+int(z[a/2:]))**2)
			if int(z)==i:
				print(i)

else:
	for i in range(10**(a-1),10**(a)):
		z=str(i)
		z=str((int(z[:a/2])+int(z[a/2:]))**2)
		if int(z)==i:
			print(i)