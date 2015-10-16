a='5 3 1 3 4'.strip().split(' ')
goal=int(a[0])
a=[int(a[i]) for i in xrange(2,len(a))]
chose=''
currently_max=0


for i in xrange(len(a)):
	round_chose=str(a[i])+' '
	round_sum=a[i]
	b=a[:]
	b.pop(b.index(a[i]))
	while b:
		round_max=max(b)
		if round_sum+round_max <= goal:
			round_chose+=str(round_max)+' '
			round_sum+=round_max
		b.pop(b.index(round_max))
	if round_sum>currently_max:
		chose=round_chose
		currently_max=round_sum
print(chose,currently_max)

'''
def findmax(i,chose,currently_num,goal,currently_max):
	if i<len(a):
		round_max=max(a[i:])
		if currently_num+round_max<=goal:
			chose+=' '+str(round_max)+' '
			currently_num+=round_max
			(chose,currently_num)=findmax(i+1,chose,currently_num,goal,currently_max)
		elif currently_num>currently_max :
			#print(chose,currently_num)
			return chose 

for i in xrange(len(a)):
	(chose,currently_num)= findmax(i+1,str(a[i]),a[i],goal,currently_max)
	print(chose,currently_num)


def findmax(getnum,currently_num,goal,maxnum):

	if currently_num+max(a)<=goal:
		getnum+=str(max(a))+' '
		currently_num+=max(a)	
	a.pop(a.index(max(a)))
	if a:
		findmax(getnum,currently_num,goal)
	else:
		if currently_num > maxnum:
			return getnum
		print('%s sum=%d ' % (getnum[::-1],currently_num))

'''