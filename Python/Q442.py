a={'A':[50,10],
   'B':[10,20],
   'C':[20,5],
   'D':[30,35],
   'E':[35,15],
   'F':[15,5],
   'G':[5,10],
   'H':[10,20],
   'I':[20,25],
}

b='((D(EF))((GH)I))'
add=0
stack=[]
for x in b:
	cal=set()
	if x =='(':
		continue
	elif x ==')':
		first=stack.pop()
		second=stack.pop()
		total=1
		cal |= set(first)|set(second)
		for i in cal:
			total*=i
		cal-=set(first).intersection(set(second))
		if list(cal) ==[] or len(cal)>2:
			print("ERROE")
			break
		stack.append(list(cal))
		add+=total
	else:
		stack.append(a.get(x))
print(add)