import math

#node=[[5,19],[55,28],[38,101],[28,62],[111,84],[43,116]]
node=[[11,27],[84,99],[142,81],[88,30],[95,38]]
#node=[[132,73],[49,86],[72,111]]
howfar=[[] for i in xrange (len(node))]
is_cycle=[i for i in xrange (len(node))]

totaldistance=0.0
outputstr=[''for i in xrange (len(node))]


def cycle(a,b):
	do=0
	g=is_cycle[b]
	if is_cycle[a] != is_cycle[b]:
		for x in xrange(len(is_cycle)):
			if is_cycle[x]==g:
				is_cycle[x]=is_cycle[a]
	else:
		print("fuck")
		do=1
	return do

for i in xrange(len(node)):
	for x in  xrange(len(node)):
		if x!=i:
			howfar[x].append( round( ((node[i][0]-node[x][0])**2+(node[i][1]-node[x][1])**2)**0.5+16,3)  )
		else:
			howfar[x].append(300)
for z in xrange(len(node)-1):
	min_of_node=[]
	
	for x in howfar:
		min_of_node.append(min(x))
	start_node=min_of_node.index(min(min_of_node))
	end_node= (howfar[min_of_node.index(min(min_of_node))].index(min(howfar[ min_of_node.index(min(min_of_node))]) ))
	
	while cycle(start_node,end_node):
		howfar[start_node][end_node]=300
		howfar[end_node][start_node]=300
		min_of_node=[]
		for x in howfar:
			min_of_node.append(min(x))
		start_node=min_of_node.index(min(min_of_node))
		end_node= (howfar[min_of_node.index(min(min_of_node))].index(min(howfar[ min_of_node.index(min(min_of_node))]) ))
	
	totaldistance+=howfar[start_node][end_node]
	outputstr[start_node]= node[start_node],node[end_node],howfar[start_node][end_node]
	howfar[start_node][end_node], howfar[end_node][start_node]=(300,300)
		
	for y in xrange(len(node)):
		howfar[start_node][y]=300
		howfar[y][end_node]=300

print("\n".join(map(str,outputstr)))
print(round(totaldistance,2))