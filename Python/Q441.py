
a=[1,2,3,4,5,6,7]
number=set()

for x in a:
	number.add(x)
visited=''
def dfs(path,next,used):
	used+=str(next)
	path+=str(next)
	for x in a:
		if len(path) == 6:
			print(path)
			break
		if str(x) not in used:
			if x > int(path[-1:]):
				dfs(path,x,used)

for i in a :
	dfs('',i,visited)