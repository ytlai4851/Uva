a=5
b=43
c=[]
d=""


if a/b==0:
	c.append(a)
	d+="0."
	a=a*10
else:
	a=a%b*10
	d+=str(a/b)+'.'


while b>0:
	d+=str((a/b))
	if a%b==0:
		d+='0'
		print(d,'1')
		break
	elif a%b not in c:
		c.append(a%b)
		a=a%b
	else:
		print(c.index(a%b))
		print(d[c.index(a%b)::],len(d)-c.index(a%b)-2)
		break

	a=a*10



