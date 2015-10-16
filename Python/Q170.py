c=['' for i in range(14)]


for i in range(4):
    a=raw_input()
    b=a.strip().split(' ')
    z=0
    for j in range(13,0,-1):
        c[j]+=(b[z])
        z+=1

pick=13
count=0
print(c)
#nextpick=int(c[pick][:2][:1])

while c[pick]!='':
    try:
        nextpick=int(c[pick][:2][:1])
    except ValueError: 
        nextpick={'T':10,'A':1,'J':11,'Q':12,'K':13}.get(c[pick][:2][:1])
    
    print(nextpick)
    print(c[pick][:2])
    c[pick]=c[pick].replace(c[pick][:2],'')
    count+=1
    pick=nextpick
    print(count)
    #print(pick)
    #print(c)

print(count)
