Z=7
I=5
M=12
L=4
count=0
historyL=[]
while L not in historyL :
	historyL.append(L)
	L=(L*Z+I)%M
	count+=1
print(L,count- historyL.index(L) )
