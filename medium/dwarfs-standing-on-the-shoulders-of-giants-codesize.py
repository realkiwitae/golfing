d=v={}
o=input
for i in range(int(o())):a,b=map(int,o().split());d.setdefault(a,[]).append(b)
r=0
while v:
 r+=1;w=[]
 for a in v:w+=d.setdefault(a,[])
 v=w
o(r)