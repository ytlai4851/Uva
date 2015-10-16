a='1 2   2 7   1 3   3 4   3 5   5 10   5 11 4 6   7 6   7 8   7 9   8 9   8  6   6 11'.strip().split(' ')
g={}

while '' in a:
	a.remove('')

b=set(a)
for i in b:
	temset=set()

	for x in xrange(0,len(a),2):
		if a[x]==i or a[x+1] ==i:
			temset.add(a[x])
			temset.add(a[x+1])
	g[i]=temset

visit=set()
def bfs(node,ttl):
	while ttl :
		ttl-=1
		for i in g[node]:
			visit.add(i)
			bfs(i,ttl)
		#print(visit)
bfs('3',3)

print(len(b-visit))