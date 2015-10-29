f=open('I:\Coding Practice\UVA\Python\Taipei1030103.txt','r')

Roulette=[]
Shooting=[]
Money=[]

for i in xrange(int(f.readline())):
	Roulette.append(int(f.readline()))
for i in xrange(int(f.readline())):
	Shooting.append(int(f.readline()))
	Money.append([Roulette[Shooting[i]]])
B=int(f.readline())

for R in xrange(0,len(Roulette)/2+1):
	tem=0
	for i in xrange(len(Shooting)):
		Money[i].extend([Roulette[(Shooting[i]-(R+1))%len(Roulette)],Roulette[(Shooting[ i]+(R+1))%len(Roulette)]])
	for i in xrange(len(Money)):
		tem+=max(Money[i])
	if tem > B:
		break
print(R)