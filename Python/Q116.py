a=[[3,4,1,2,8,6],[6,1,8,2,7,4],[5,9,3,9,9,5],[8,4,1,3,2,6],[3,7,2,1,2,3]]
#a=[[3,4,1,2,8,6],[6,1,8,2,7,4],[5,9,3,9,9,5],[8,4,1,3,2,6],[3,7,2,8,6,4]]
totoa=[[]for i in range(len(a[0])-1)]
path=[[]for i in range(len(a[0])-1)]
for i in range(5,0,-1):
	for j in range(len(a)):
		c=[a[(j+5-1)%5][i],a[j][i],a[(j+5+1)%5][i]]
		a[j][i-1]+=min(c)
		totoa[i-1].append(a[j][i-1])
		path[i-1].append({0:(j+5-1)%5 ,1:j, 2:(j+5+1)%5 }.get(c.index(min(c))))
print(path)

print(totoa)

out=''
out+=str(totoa[0].index(min(totoa[0]))+1)
next=totoa[0].index(min(totoa[0]))
for i in range(len(path)):
	out+=str(path[i][next]+1)
	next=path[i][next]

print(out)


	