a=['999','1']
max_length=len(max(a,key=len))
tem=0
carry=0

for i in xrange(len(a)):
	while len(a[i])<max_length:
		a[i]='0'+a[i]

for x in xrange(len(a)):
	a[x]=a[x][::-1]
out=''

for x in xrange(max_length):
	for i in a:
		tem+=int(i[x])
		print(i[x],carry)
	tem+=carry
	carry=0
	print(tem)
	if tem>9:
		carry=tem/10
	out=str(tem%10)+out
	tem=0
if carry > 0:
	out=str(carry)+out
print (out)