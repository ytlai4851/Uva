board=[[0 for x in xrange(8)] for i in xrange(8)]
direction=[[-2,-1],[-1,-2],[1,-2],[2,-1],[1,2],[2,1],[-2,1],[-1,2]]
startp=[0,0]
endp=[7,6]
knightpoint=[]
addnode=[1]
t=0
zz=0
board[startp[0]][startp[1]]=1
knightpoint.append(startp)
for i in knightpoint:
	t+=1
	for j in direction:
		x=i[0]+j[0]
		y=i[1]+j[1]
		if x < 0 or x>7 or y<0 or y>7 or [x,y] in knightpoint :
			continue
		board[x][y]=1
		knightpoint.append([x,y])
		zz+=1
	if t==addnode[len(addnode)-1]:
		addnode.append(zz)
		zz=0
		t=0
	if endp in knightpoint:
		break
print(addnode)
print("\n".join(map(str,board)))
