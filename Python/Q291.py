a=[[],[2,3,5],[1,3,5],[1,2,4,5],[3,5],[1,2,3,4]]
b=[[0 for j in xrange(6)] for x in xrange(6)]
path_recoed=''
def path(path_recoed,node):
	path_recoed+=str(node)
	for x in a[node]:
		if b[node][x]==0:
			(b[node][x] ,b[x][node])=(1,1)
			#print(node,x)
			path(path_recoed,x)
			(b[node][x] ,b[x][node])=(0,0)
	if len(path_recoed)==9:
		print(path_recoed)
path(path_recoed,1)