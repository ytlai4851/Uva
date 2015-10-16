def longest_increasing_subsequence(d):
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) + [d[i]])
        print(l)
    return max(l, key=len)




#print(longest_increasing_subsequence([6,2,3,5]))