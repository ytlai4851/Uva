cycle=[]
b=2374859
p=3029382
m=36123
for x in xrange(1,10000):
	if (b**x)%m in cycle :
		break
	else:
		cycle.append((b**x)%m)

print(cycle[p%(x-1)-1])
