import datetime

a=[90,75,72,60,50,40,24,18]
gap=a[:]
s=["r" for i in xrange( len(a))]

for x in xrange(len(a)):
	a[x]=a[x]*2


for x in xrange(18000):
	for i in xrange(len(a)):
		if x==a[i]:
			if s[i]=="r":
				s[i]="g"
				a[i]=a[i]+gap[i]-5
			else:
				s[i]="r"
				a[i]=a[i]+gap[i]+5
	if "r" not in s:
		print(datetime.timedelta(seconds=x))
		break 
	elif x==18000:
		print("88")

	
		

