a={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
b='IV'
tem=[]
for i in b :
	tem.append(a.get(i))

print(tem)