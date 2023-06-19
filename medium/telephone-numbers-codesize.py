d,r={},0
_,*t=open(0)
for a in t:
 u=d
 for b in a.strip():r+=u.get(b,1)==1;u=u.setdefault(b,{})
print(r)