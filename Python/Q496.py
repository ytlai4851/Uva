a={1,2}
b={2,3}

if a==b:
	print("A equals B")

elif len(a|b) == len(a)+len(b):
	print("A and B are disjoint")

elif len(a|b) < len(a)+len(b):
	if len(a^b)>1:
		print("I'm confused!")
	elif len(a)>len(b):
		print("B is a proper subset of A")
	else:
		print("A is a proper subset of B")
