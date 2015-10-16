#-*- coding: UTF-8 -*-
'''
a=[['ben','alex'],['alex','dol'],['dol','ben'],['dol','bene'],['bene','dol'],['alex','aar']]
'''
a=[['John','Aaron'],['Aaron','Benedict'],['Betsy','John'],['Betsy','Ringo'],['Ringo','Dolly'],['Benedict','Paul'],
['John','Betsy'],['John','Aaron'],['Benedict','George'],['Dolly','Ringo'],['Paul','Martha'],['George','Ben'],['Alexander','George'],
['Betsy','Ringo'],['Alexander','Stephen'],['Martha','Stephen'],['Benedict','Alexander'],['Stephen','Paul'],['Betsy','Ringo'],
['Quincy','Martha'],['Ben','Patrick'],['Betsy','Ringo'],['Patrick','Stephen'],['Paul','Alexander'],['Patrick','Ben'],['Stephen','Quincy'],
['Ringo','Betsy'],['Betsy','Benedict'],['Betsy','Benedict'],['Betsy','Benedict'],['Betsy','Benedict'],['Betsy','Benedict'],
['Betsy','Benedict'],['Quincy','Martha']]
#'''
totalname=[]
cycle_path=[]

for x in a:
	for i in x:
		if i not in totalname :
			totalname.append(i)

call_list=[[] for i in xrange(len(totalname))]
group=[-1 for i in xrange( len(totalname))]

for x in xrange(len(a)):
	if totalname.index(a[x][1]) not in call_list[totalname.index(a[x][0])] :
		call_list[totalname.index(a[x][0])].append(totalname.index(a[x][1]))

visit=[1 for i in xrange (len(totalname))] #能走的
final_path=[]

def groupall(out,i,x):
	while out[i]!=x:
		group[i]=x
		i=out.index(group[i])

def dfs(out,i):
	for x in call_list[i]:
		if i ==0:
			out=''
			out+=str(i)+' '
		if str(x) not in out:
			visit[x]=0
			out+=str(x)+' '     #================================>問題
			dfs(out,x)
		else:
			tem=out+str(x)
			cycle_path.append(map(int ,tem.strip().split(' ')))


for x in xrange(len(call_list)):
	out=''
	if visit[x]:
		visit[x]=0
		dfs(out,x)

for x in cycle_path:
	start= x.index(x[len(x)-1])
	for i in xrange(start ,   len(x)   ):
		if group[x[start]]==-1:
			group[x[i]]=x[start]
		else:
			group[x[i]]=group[x[len(x)-1]]

calling_circles=[]
for x in xrange(len(group)):
	if group[x]== -1:
		calling_circles.append([totalname[x]])
	elif group[x]!=99:
		groupn= group[x]
		tem=''
		for i in xrange(len(group)):
			if group[i]==groupn:
				tem+=totalname[i]+','
				group[i]=99
		calling_circles.append([tem])
print("\n".join(map(str,calling_circles)))

		