a="5 1 2 3 4".strip().split(' ')

g={}

#g[a[0]]=(a[i] for i in xrange(len(a)-1))
g.update({a[0]:a[i] for i in xrange(len(a))})

print(g)