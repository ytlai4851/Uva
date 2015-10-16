#-*- coding: UTF-8 -*-
stick=[[],[],[]]
n=100 #dish count
m=12345678901234567890#move times
print(type(m))
stick[0].extend([i+1 for i in xrange (n)])

def move_dish(dishn,stickn):        #dishn=2 stickn=0
	dishn_ar=stickn	

	do=0
	for x in xrange(1,4):
		if  stick[(stickn+x)%3]==[]  or   stick[(stickn+x)%3][0]>dishn :
			stick[(stickn+x)%3].insert(0,stick[dishn_ar].pop(0))
			do=1
			break
		else:
			do=0
	return do 

for x in xrange(1,m+1):
	do=0
	if x%2==0:
		for i in xrange(len(stick)) :
			if 1 not in stick[i]  and stick[i]!=[]:
				for j in stick[i]:
					do=move_dish(j,i)
					if do :
						break
			if do :
				break

	else:
		for i in xrange(len(stick)):
			if 1 in stick[i]:
				stick[(i+1)%3].insert(0,stick[i].pop(0))
				break
for x in stick:
	print(len(x))
				