a = '0 0 0 1 22 -333 0 1 -1'
a=a.strip().split(' ')
st=''
for i in range(len(a)):

	if int(a[i])>0 :
		if int(a[i])==1:
			st+='+'+'x'+'^'+str(len(a)-1-i)
			if str(len(a)-1-i)=='1' or str(len(a)-1-i)=='0':
				st=st.rstrip(str(len(a)-1-i))
		else :
			st+='+'+str(a[i])+'x'+'^'+str(len(a)-1-i)
			if str(len(a)-1-i)=='1 'or str(len(a)-1-i)=='0':
				st=st.rstrip(str(len(a)-1-i))
	elif int(a[i])<0:
		st+=str(a[i])+'x'+'^'+str(len(a)-1-i)
		if str(len(a)-1-i)=='1' or str(len(a)-1-i)=='0':
			st=st.rstrip(str(len(a)-1-i))
st=st.lstrip('+')
print(st)