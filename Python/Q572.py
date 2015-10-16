g=['*@*@*','**@**','*@*@*']
#g=['@@****@*']
#g=['****@','*@@*@','*@**@','@@@*@','@@**@']
move=[[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1],[1,1],[-1,-1]]
deposit_c=0


def find(g,i,j):
	print(i,j)
	for x in move:
		try:
			if g[i+x[0]][j+x[1]]=='@'  and i+x[0]>=0 and j+x[1]>=0:
				print(g[i+x[0]][:j+x[1]+1])
				g[i+x[0]]=g[i+x[0]][:j+x[1]]+g[i+x[0]][j+x[1]:j+x[1]+1].replace('@',str(deposit_c))+g[i+x[0]][j+x[1]+1:]
				find(g,i+x[0],j+x[1])
		except IndexError :
			pass
	pass


for i in xrange(len(g)):
	for j in xrange( len(g[i])):
		if g[i][j] =='@':
			g[i]=g[i][:j+1].replace('@',str(deposit_c))+g[i][j+1:]
			find(g,i,j)
			print(g)
			deposit_c+=1
print(deposit_c)


