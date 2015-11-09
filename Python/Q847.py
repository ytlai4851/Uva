n=34012226
p=1
who=1
if n < 9:
	print("stan wins.")
elif n < 19:
	print("Ollie wins.")
else:
	while True:
		if who %2 :
			p*=2
		else:
			p*=9
		if float(n)/float(p)<=9:
			if who %2 :
				print("Ollie wins.")
			else:
				print("stan wins.")
				
			break
		who+=1
		print(who,p)
