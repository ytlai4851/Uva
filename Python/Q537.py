a='A light-bulb yields P=100W and the voltage is U=220V. Compute the current, please.'
function={}
do=0
zz=''
tem=''
for i in xrange(len(a)) :
	if a[i-1] =='=' and a[i].isdigit() :
		zz=a[i-2]
		do=1
	if do:
		if a[i] =='.':
			tem+=a[i]
		elif not a[i].isdigit():
			do=0	
			tem=float(tem)
			if a[i] =='m':
				function[zz]=tem/1000
			elif a[i] =='k':
				function[zz]=tem*1000
			elif a[i] == 'M':
				function[zz]=tem*1000000
			else:
				function[zz]=tem
			tem=''		
		else:
			tem+=a[i]

if 'P' not in function:
	print(function['I']*function['U'])
elif 'U' not in function:
	print(function['P']/function['I'])
else :
	print(function['P']/function['U'])
