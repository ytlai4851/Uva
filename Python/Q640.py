import time
start_time = time.time()
a=[i for i in xrange(10000)]

for i in xrange(10000):
	tem=i
	while i:
		tem+=i%10
		i/=10
	if tem>=10000:
		break
	try:
		a.pop(a.index(tem))
	except Exception:
		pass
print(a)

print("--- %s seconds ---" % (time.time() - start_time))


'''
for i in xrange(100):
	tem=i
	while i:
		tem+=i%10
		i/=10
	if tem>=len(a):
		break
	a[tem]=0
for i in xrange(len(a)):
	if a[i] :
		print(i)
'''
print("--- %s seconds ---" % (time.time() - start_time))

