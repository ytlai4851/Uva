from sympy import Line, Point
a='0.0 -0.5 0.5 0.0 0.0 0.5'.strip().split(' ')

p=[0,0,0]
l=[0,0,0]
for x in xrange(0,len(a)+1/2,2):
	point1=a[x]
	point2=a[x+1]
	p[x/2]=Point(point1,point2)

print(p)

for x in xrange(3):
	l[x]=Line(p[x],p[(x+1)%3])


smaepoint= l[0].intersection(l[1],l[2])