from sympy import Line, Point
f=open('D:\UVA\Python\Q378.txt','r')
while f:
	a=f.readline().strip().split(' ')
	if a ==['']:
		break
	p1,p2,p3,p4=Point(int(a[0]),int(a[1])),Point(int(a[2]),int(a[3])),Point(int(a[4]),int(a[5])),Point(int(a[6]),int(a[7]))
	l1=Line(p1,p2)
	l2=Line(p3,p4)



	if l1.is_similar(l2):
		print("LINE")
	elif Line.is_parallel(l1,l2):
		print("NONE")
	elif Line.are_concurrent(l1,l2):
		smaepoint= l1.intersection(l2)
		print("POINT %.2f %.2f " %(smaepoint[0].x,smaepoint[0].y))
	
print("END OF OUTPUT")