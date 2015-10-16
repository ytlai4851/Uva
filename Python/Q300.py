haab=[]
tzokin=[]


for j in range(19):
	if j ==18:
		for i in range(1,5):
			haab.append(i)
	else:
		for i in range(1,20):
			haab.append(i)
#print(haab)


for i in range(1,14):
	for j in range(0,20):
		tzokin.append({0:'imix', 1:'ik', 2:'akbal',3: 'kan',4: 'chicchan',5: 'cimi',6: 'manik',7: 'lamat',8: 'muluk',9: 'ok',10: 'chuen',11: 'eb',12: 'ben',13: 'ix',14: 'mem',15: 'cib', 
		16:'caban', 17:'eznab', 18:'canac', 19:'ahau'}.get(j))
#print(tzokin)	



d=10
m='zac'
m={'pop':0, 'no':1, 'zip':2, 'zotz':3, 'tzec':4, 'xul':5, 'yoxkin':6, 'mol':7, 'chen':8, 'yax':9, 'zac':10, 'ceh':11, 'mac':12, 'kankin':13, 
'muan':14, 'pax':15, 'koyab':16, 'cumhu':17, 'uayet':18}.get(m)
y=0

count=0
cy=(y*365+count+d+((m)*20))//260
count=(y*365+count+d+((m)*20))%260
translater=str((count%13)+1)+str(tzokin[count])+' '+str(cy)
print(count,translater)
