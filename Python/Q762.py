f=open('I:\\Coding Practice\\UVA\\Python\\Q762.txt','r')
road={}
for i in xrange(int(f.readline())):
	a=f.readline().strip().split(' ')
	for j in xrange(len(a)):
		if a[j] in road:
			road[a[j]].append(a[1-j])
		else:
			road[a[j]]=[a[1-j]]
print(road)

zz=(f.readline().strip().split(' '))
Started,Goal=zz[0],zz[1]
Passed=[Started]
Previous=[Started]

for i in Passed:
	for j in set(road[i])-set(Passed):
		Passed.append(j)
		Previous.append(i)
	if Goal in Passed:
		Drive_Road=[Goal]
		while True:
			need=Previous[Passed.index(Drive_Road[-1])]
			Drive_Road.append(need)
			if need == Started:
				break
		break
Drive_Road.reverse()
print(Drive_Road)