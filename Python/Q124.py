a="a b f g"
b="a b b f"

b=b.strip().split(" ")

order=[]

for i in range(len(b)/2):
	big=b[i*2+1]
	small=b[i*2]
	if len(order)==0:
		order.append([small])
		order.append([big])
	else:
		for j in range(len(order)):
			if big in order[j]:
				if j-1 <0:
					order.insert(0,[small])
				else:
					order[j-1].append(small)
				order[j-1].sort()
				break
			elif small in order[j]:
				if j+1 >len(order)-1:
					order.insert(len(order)-1,[big])
				else:
					order[j+1].append(big)
				break



print(order)