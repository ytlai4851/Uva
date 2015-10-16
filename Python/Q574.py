import itertools

a='400 12 50 50 50 50 50 50 25 25 25 25 25 25'.strip().split(' ')
goal=int(a.pop(0))
a.pop(0)
same=[]

def sumit (currently_sum,from_where,previous,goal):

	for i in xrange(from_where,len(a)):
		currently_sum+=int(a[i])
		if currently_sum<=goal:	
			previous+='+'+a[i]
			if currently_sum == goal:
				return previous
		else:
			currently_sum-=a[i]
		sumit(currently_sum,i+1,previous,goal)



for i in xrange(len(a)):
	if int(a[i]) < goal:
		print(sumit(int(a[i]),i+1,a[i],goal))