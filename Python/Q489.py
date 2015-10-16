hadguest=set()

Ans='cheese'
print(Ans)
x=0
while x <7	:
	guest=raw_input()
	if guest not in hadguest:
		if guest not in Ans:
			x+=1
		hadguest.add(guest)
	if set(Ans)==hadguest:
		print("you win")
		break