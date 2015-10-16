queens=[20,20,20,20,20,20,20,20]
plus=[20,20,20,20,20,20,20,20]
minus=[20,20,20,20,20,20,20,20]
row , col =(0,1)


def move(queens,row):
	for x in xrange(8):
		if x not in queens:
			if row+x not in plus and row-x not in minus :
				queens[row]=x
				plus[row]=row+x
				minus[row]=row-x
				#print(row,x)
				#print(queens)
				#print(plus)
				#print(minus)
				if row!=7:
					move(queens,row+1)
		if x==7 :
			queens[row]=20
			plus[row]=20
			minus[row]=20
		if 20 not in queens:
			print(queens)
			#print(x)



queens[row]=col
plus[row]=row+col
minus[row]=row-col
move(queens,row+1)


#print("\n".join(map(str,board)))