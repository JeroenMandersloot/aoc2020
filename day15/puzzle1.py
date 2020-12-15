from collections import defaultdict

l = [2,1,10,11,0,6]

d = defaultdict(list)
for i, c in enumerate(l):
    d[c].append(i)

a = 2020
n = l[-1]
for i in range(len(l), a):
    if len(d[n]) == 1:
        n = 0
    else:
        n = d[n][-1] - d[n][-2]
    d[n].append(i)

print(n)
       
    