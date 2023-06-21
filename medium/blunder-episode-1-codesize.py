Z=input
h,w=map(int,Z().split())
M=[]
T=[]
o=b=d=0
for i in range(h):
 M+=[[]]
 for c in Z():
  M[-1]+=[c]
  if c=='@':S=(i,len(M[-1])-1)
  if c=='T':T+=[[i,len(M[-1])-1]]
s=["SOUTH","EAST","NORTH","WEST"]
D=[(1,0),(0,1),(-1,0),(0,-1)]
P=[]
V=[]
def A(u,v):return[u[0]+v[0],u[1]+v[1]]
def m(p):return M[p[0]][p[1]]
def r():
 for i in range(4):
  a=i*(not o)+(3-i)*o
  if m(A(S,D[a]))not in'#'+'X'*(not b):return a
while(S[0],S[1],d,o,b)not in V:
 V+=[(S[0],S[1],d,o,b)];n=A(S,D[d]);v=m(n)
 if v=='B':b=not b
 if v=='I':o=not o
 if v=='T':S=A(T[n!=T[1]],D[(d+2)%4])
 if v=='$':Z("\n".join(P+[s[d]]));exit()
 if v=='#':d=r();continue
 if v=='X':
  if b:M[n[0]][n[1]]=' ';V=[]
  else:d=r();continue
 S=A(S,D[d]);P+=[s[d]];v=m(S)
 if v in"SENW":d="SENW".find(v)
Z("LOOP")