box_total=[41,61,36,90,54,66]

used_box=0

used_box+=box_total[5]+box_total[4]+box_total[3]
box_total[0]-=box_total[4]*11
box_total[1]-=box_total[3]*5

used_box+=box_total[2]/4
if box_total[2]%4:
	used_box+=1

if box_total[2]==3:
	box_total[0]-=5
	box_total[1]-=1
elif box_total[2]==2:
	box_total[1]-=3
	box_total[0]-=6
elif box_total[2]==1:
	box_total[1]-=5
	box_total[0]-=7

if box_total[1]>0:
	used_box+=box_total[1]/9
	if box_total[1]%9:
		used_box+=1
elif box_total[1]<0:
	box_total[1]-=(-box_total[2])*4

if box_total[0]>1:
	used_box+=box_total[1]/36
	if box_total[1]%36 :
		used_box+=1

print(used_box)