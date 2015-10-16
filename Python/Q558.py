path={0:{1:10},
	1:{2:20},
	2:{1:30},
	3:{0:-60},
}



def dfs(start,visit):
	for i in path[start]:
		if str(i) in visit:
			print(start,visit)
			pathl=0
			for x in  visit[visit.index(str(i)):]:
				pathl+=path[int(x)][start]
			if pathl > pathl+path[start][int(visit[-1])]:
				print('have')
			else:
				print('NO')
			break
		visit+=str(start)
		dfs(i,visit)


dfs(0,'')


#print(path)