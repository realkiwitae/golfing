d={}
o=input
for i in range(int(o())):a,b=map(int,o().split());d.setdefault(a,[]).append(b)
def f(d,i):return 1+max(f(d,j)for j in d[i])if i in d else 0
o(1+max(f(d,i)for i in d))