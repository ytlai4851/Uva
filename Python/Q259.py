a=[[1,1],[2,2],[3,3],[9,10],[10,11]]
#a=[[1,2],[3,4]]
m_list=[[]  for i in xrange(len(a))]
mix=0

for i in xrange(len(a)):
	inedx=0
	temmin=0
	for x in xrange(len(a)):
		if x != i:
			m_list[i].append(float((a[x][1]-a[i][1]))/float((a[x][0]-a[i][0])))
			m_list[i].sort()
	for x in xrange(len(m_list[i])):
		if m_list[i][x]==m_list[i][inedx] :
			temmin+=1
			#print(m_list[i][x])
		else:
			temmin=1
			inedx=x
		if temmin>mix:
			mix=temmin

print(mix+1)


