s=lambda:input().split()
*_,f,p,c,a,n=s()
t={f:p}
t.update(s()for j in['']*int(n))
while 1:f,p,d=s();print(('BLOCK','WAIT')['-'in p or(int(p)-int(t[f]))*d.find('I')<=0])