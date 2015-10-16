a=[['s....','.###.','.##..','###.#'],['#####','#####','##.##','##...'],['#####','#####','#.###','####E']]
move=[[-1,0,0],[1,0,0],[0,0,1],[0,0,-1],[0,1,0],[0,-1,0]]
walk=['000']

#print(a[0][3][2])


#while True:
for j in walk:
	for i in move:
		z=int(j[0])+i[0]
		if z <0 or z>len(a)-1:
			continue
		x=int(j[1])+i[1]
		if x <0 or x>3:
			continue
		y=int(j[2])+i[2]
		if y <0 or y>4:
			continue
		print(z,x,y,j)
		if  y >=0 and x>=0:
			next=a[z][x][y]
			if str(z)+str(x)+str(y) not in walk and next == '.':
				walk.append(str(z)+str(x)+str(y))
				print(walk)
		if next=='E':
			print(next)
			walk.append('E')
			break
	if 'E' in walk:
		break