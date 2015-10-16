a= "2 0.318".strip().split(" ")

j=int(a[0])
k=len(a[1])-j-2

top=int(10**(k+j)*float(a[1]) - int((10**k)*float(a[1])))
down=10**(k+j) - 10**k

b=top
c=down

while b and c :

	if b<c:
		c-=(c/b)*b

	else:
		b-=(b/c)*c

top, down = (top/max(c,b) , down/max(c,b))

print(top,down)