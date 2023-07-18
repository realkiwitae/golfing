from copy import deepcopy as D
o=range
w,h=map(int,input().split())
class Z():
 def __init__(S,G=None,r=0,b=0):
  if G is None:
   S.M=[[c for c in input().strip()]for i in o(h)];S.E=[];S.B=[];S.T=[]
   for i in o(h):
    for j in o(w):
     if S.M[i][j]=='@':S.T+=[(i,j)]
  else:S.M=D(G.M);S.E=D(G.E);S.B=D(G.B);S.T=D(G.T)
  S.w=len(S.T);S.d=[[[]for j in o(w)]for i in o(h)];S.top3=None;S.r=r;S.b=b

 def Y(S,A):
  if A.action[0]=='WAIT':
   if len(S.B)<1:return"WRONG MOVE"
   while len(S.B)>0:
    for b in S.B:
     j=int(S.M[b[0]][b[1]][1:])-1;S.M[b[0]][b[1]]='B'+str(j)
     if j<1:S.X(*b)
  else:
   S.B+=[(A.B[0],A.B[1])];S.E+=A.B[-1]
   for e in A.B[-1]:
    if e in S.T:S.T.remove(e)
    else:0
   S.M[A.B[0]][A.B[1]]='B3';S.b+=1
 def P(S):
  S.d=[[[]for j in o(w)]for i in o(h)]
  for t in S.T:S.L(*t,S.Q)
  return[r for r in sorted([(i,j,S.d[i][j])for j in o(len(S.d[0]))for i in o(len(S.d))],key=lambda x:-len(x[2]))[:3]if len(r[2])>0]
 def X(S,x,y,p=0):
  if S.M[x][y][0]=='B':S.M[x][y]='.';S.L(x,y,S.X);S.B.remove((x,y))
  if S.M[x][y]=='@':S.E.remove((x,y))
  S.M[x][y]='.'
 def Q(S,x,y,p):
  if S.M[x][y]!='@':S.d[x][y]+=[p]
 def L(S,x,y,f):
  c=[1]*4
  for i in o(4):
   if x+i>h-1 or S.M[x+i][y]=='#':c[0]=0
   if c[0]:f(x+i,y,(x,y))
   if x-i<0 or S.M[x-i][y]=='#':c[1]=0
   if c[1]:f(x-i,y,(x,y))
   if y+i>w-1 or S.M[x][y+i]=='#':c[2]=0
   if c[2]:f(x,y+i,(x,y))
   if y-i<0 or S.M[x][y-i]=='#':c[3]=0
   if c[3]:f(x,y-i,(x,y))
class A():
 def __init__(S,a=[],t=3):S.action=["WAIT"]*t if len(a)<1else[' '.join(map(str,a[:-1][::-1]))];S.B=a
def solver(G):
 r=[([],G)]
 if G.w==0:return[]
 n=0
 while 1:
  n+=1;l=[];idx=-1
  for a,m in r:
   t=min([int(m.M[b[0]][b[1]][1:])for b in m.B]or[0])
   if t:
    k=Z(m,r=n);j=A(t=t);k.Y(j)
    if len(k.T)<1:return a+[j],k
    l+=[[a+[j],k]]
   tmp=m.P()
   for b in tmp:
    k=D(m);j=A(b);k.Y(j)
    if len(k.T)<1:return a+[j],k
    l+=[[a+[j],k]]
  r=l
G=Z(G=None,r=0,b=0)
R,k=solver(G)
actionToPrint=[a for r in R for a in r.action]
n=-1
while 1:n+=1;rounds,B=map(int,input().split());print(actionToPrint[n]if n<len(actionToPrint)else"WAIT")
