import time
import datetime as d

charing=input()
start=raw_input()
end=raw_input()
mt=[0.0,0.0,0.0,0.0]
start=d.datetime.strptime(start,'%H %M')
end=d.datetime.strptime(end,'%H %M')
endtime=['18 00','22 00','08 00']
for i in range(0,3):
	endtime[i]=d.datetime.strptime(endtime[i],'%H %M')

cost=[[0.1,0.06,0.02],[0.25,0.15,0.05],[0.53,0.33,0.13],[0.87,0.47,0.17],[1.44,0.80,0.30]]


temstart=start
tem=d.datetime.strptime('00 00','%H %M')


if end<start:
	while temstart != tem:
		if   temstart>=d.datetime.strptime('08:00','%H:%M')  and  temstart<d.datetime.strptime('18:00','%H:%M'):
			startse=0
		elif temstart>=d.datetime.strptime('18:00','%H:%M')  and  temstart<d.datetime.strptime('22:00','%H:%M') :
			startse=1
		else:
			startse=2



		if startse!=2:
			mt[3]=(endtime[startse]-temstart).total_seconds()/60*cost[charing][startse]+mt[3]
			mt[startse]=(endtime[startse]-temstart).total_seconds()/60+mt[startse]
			temstart=endtime[startse]
			print(mt)
		else:
			zzz=tem-temstart
			mt[3]=zzz.seconds/60*cost[charing][startse]+mt[3]
			mt[startse]=zzz.seconds/60+mt[startse]
			temstart=tem
			print(mt)
			print('OK')

	while temstart != end:
		if   temstart>=d.datetime.strptime('08:00','%H:%M')  and  temstart<d.datetime.strptime('18:00','%H:%M'):
			startse=0
		elif temstart>=d.datetime.strptime('18:00','%H:%M')  and  temstart<d.datetime.strptime('22:00','%H:%M') :
			startse=1
		else:
			startse=2

		if end>endtime[startse]:
			mt[3]=(endtime[startse]-temstart).total_seconds()/60*cost[charing][startse]+mt[3]
			mt[startse]=(endtime[startse]-temstart).total_seconds()/60+mt[startse]
			temstart=endtime[startse]
		else:
			mt[3]=(end-temstart).total_seconds()/60*cost[charing][startse]+mt[3]
			mt[startse]=(end-temstart).total_seconds()/60+mt[startse]
			temstart=end
		print(mt)
else:
	while start != end:
		if end>start:
			if   start>=d.datetime.strptime('08:00','%H:%M')  and  start<d.datetime.strptime('18:00','%H:%M'):
				startse=0
			elif start>=d.datetime.strptime('18:00','%H:%M')  and  start<d.datetime.strptime('22:00','%H:%M') :
				startse=1
			else:
				startse=2

			if end>endtime[startse]:
				mt[3]=(endtime[startse]-start).total_seconds()/60*cost[charing][startse]+mt[3]
				mt[startse]=(endtime[startse]-start).total_seconds()/60
				start=endtime[startse]
			else:
				mt[3]=(end-start).total_seconds()/60*cost[charing][startse]+mt[3]
				mt[startse]=(end-start).total_seconds()/60
				start=end
			print(mt)

print(mt)

