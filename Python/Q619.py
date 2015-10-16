a='28011622636823854456520'

if a[0].isdigit():
	a=int(a)
	s=[]
	while a !=0:
		s.append(chr(a%26+96))
		a/=26
	print(''.join(s[::-1]))
else:
	num=0
	a=a[::-1]
	for i in xrange(len(a)):
		num+=(ord(a[i])-96)*26**i
	print(num)
