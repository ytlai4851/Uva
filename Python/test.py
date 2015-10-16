

a='10 4 9 8 4 2'.strip().split(' ')
goal=int(a[0])
a=[int(a[i]) for i in xrange(2,len(a))]
b=''
print(a[-1])
print(a[2:])
print(max(a[2:]))

#print(max(a[i for i in xrange(1,3)]))