#-*- coding: UTF-8 -*-

graph = {0 : [1,2,8],
         1 : [0,2,3],
         2 : [0,1,5],
         3 : [1,4,10],
         4 : [3,5,6],
         5 : [2,4,7,12],
         6 : [4,8],
         7 : [5,9],
         8 : [0,6,9],
         9 : [7,8,11,13],
         10 : [3,11,13],
         11 : [9,10,12],
         12 : [5,11,13],
         13 : [9,10,12],
}
def floydwarshall(start,end):
	dist={}
	pred={}
	path={}
	for i in graph:
		dist[i] = {}
		pred[i] = {}
		for x in graph:
			pred[i][x]=-1

	print(pred)
	for i in xrange(5):
		pass


floydwarshall(1,8)