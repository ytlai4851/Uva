'''c=1
number=2

def judgy(a):
	b=0
	while b<1:
		if a%2==0:
			a=a/2
		elif a%3==0:
			a=a/3
		elif a%5==0:
			a=a/5
		if a==1:
			b=1
			break
		else :
			break
	return(b)	




while c < 1500:
	b=judgy(number)
	if b:
		c+=1	
	number+=1
print(number)
	
'''
def ugly(n):
	c2,c3,c5=(0,0,0)
	ugly=[ 1 for i in xrange(n) ]
 
	nx_2,nx_3,nx_5=(2,3,5)
	for i in xrange(1,n):
 
		ugly[i]=min(nx_2,nx_3,nx_5)
 
		if ugly[i]==nx_2:
			c2+=1
			nx_2=ugly[c2]*2
		if(ugly[i]==nx_3):
			c3+=1
			nx_3=ugly[c3]*3
		if ugly[i]==nx_5:
			c5+=1
			nx_5=ugly[c5]*5
 
	return ugly[n-1]
 
num=int(raw_input('Enter the n'))
print ugly(num)