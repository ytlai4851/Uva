a=[3,1,2,4,9,5,10,6,8,7]
b=[1,2,3,4,5,6,7,8,9,10]
c=[4,7,2,3,10,6,9,1,5,8]
d=[3,1,2,4,9,5,10,6,8,7]

#8, 3, 4, 1, 9, 6, 2, 10, 7, 5

orderevnet=[0 for i in range(10)]
length=[[] for i in range(len(orderevnet))]
print(length)


for i in range(10):
	orderevnet[c[i]-1]=i+1
	
for i in range(len(orderevnet)-1):
	for j in range(i+1,len(orderevnet)):
		if a.index(orderevnet[i])<a.index(orderevnet[j]):
			length[orderevnet[i]-1].append(orderevnet[j])
print(length)
