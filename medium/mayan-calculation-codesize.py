I=input
R=range
l,h=map(int,I().split())
def B(n,b): 
 q=-1;o='' 
 while q!=0:q=n//b;r=n%b;o=d[r]+o;n=q 
 return o
def U():return sum((20**i)*[*d.keys()][[*d.values()].index('\n'.join(I()for j in R(l))+'\n')]for i in R(int(I())//l-1,-1,-1))
d=dict(zip(R(20),['']*20))
for i in R(h):
 n=I()
 for j in R(20):d[j]+=n[j*l:(j+1)*l]+'\n'
a=U()
b=U()
I(B(eval(str(a)+I()+str(b)),20))