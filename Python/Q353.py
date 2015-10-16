a='madam'
haverecord=[]
cont=0
for i in range(len(a)):
	tem1=''
	for j in range(i,len(a)):
		tem1+=a[j]
		if tem1 == tem1[::-1]:
			if tem1 not in haverecord:
				print(tem1)
				cont+=1
				haverecord.append(tem1)
print(cont,haverecord)