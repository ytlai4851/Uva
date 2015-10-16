a=[[1,11,5],[2,6,7],[3,13,9],[12,7,16],[14,3,25],[19,18,22],[23,13,29],[24,4,28]]

hight=[0 for i in range(0,50) ]
maxhigh=0
R=0
for i in a :
	L=i[0]
	H=i[1]
	R=i[2]
	for j in range(L,R):
		if hight[j]<H:
			hight[j]=H
output=''
for i in range(1,len(hight)-1):
	if hight[i-1]!=hight[i]:
		output+=str(i)+' '+str(hight[i])+' '
print(hight)
print(output)