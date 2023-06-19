_,*i=[map(int,x.split())for x in open(0)]
X,Y=zip(*i)
v=sorted(Y)[len(Y)//2]
print(max(X)-min(X)+sum(abs(v-y)for y in Y))