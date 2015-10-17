#a=rnput()
a='8:11'

b=a.strip().split(':')

c=(int(b[0])*5-int(b[1]))*6
#print (c)
if c>180:
	c=360-c
	
print(c)