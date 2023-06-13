r=""
p=k=-1
for c in input():
 for j in range(6,k,k):
  b=ord(c)>>j&1
  if b!=p:r+=" "*(p>k)+"0"*(b<1)+"0 ";p=b   
  r+="0"
print(r)