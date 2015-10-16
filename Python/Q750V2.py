def per(queens,row):
	for x in xrange(8):
		queens[row]=x
		if is_attack(queens,row):
			if row==7:
				pass
			else:
				per(queens,row+1)
		
def is_attack(queens,row):
	
queens=[20,20,20,20,20,20,20,20]
for i in xrange(8):
	queens[0]=i  '''index of queen'''
	per(queens,1)