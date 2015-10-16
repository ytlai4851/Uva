Newspapers=[1,2,3,4]
sub=''

def com(s,sub):
	sub+=str(Newspapers[s])
	if len(sub)<2:
		for i in xrange(s,len(Newspapers)-1):
			com(i+1,sub)
	else:
		print(sub)

for i in xrange(len(Newspapers)):
	com(i,sub)