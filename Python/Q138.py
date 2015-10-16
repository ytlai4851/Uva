'''
streetlong=1
a=0
while a<10:
	stree=[i for i in xrange(streetlong+1)]
	recordtag=[1,streetlong]
	for x in xrange(streetlong/2):
		target=(min(recordtag)+max(recordtag))/2
		#left=0
		#right=0
		left=(target)*(target-1)/2
		right=(1+streetlong)*streetlong/2-left-target
		if left==right:
			a+=1
			print(target,streetlong)
			break
		elif left<right:
			recordtag[0]=target
		elif left>right:
			recordtag[1]=target
	streetlong+=1
'''
streetlong=1
z=0
while z <10:
	streetlong+=1
	last=(-1+(1+8*streetlong**2)**0.5)/2

	if last.is_integer():
		print(streetlong,last)


