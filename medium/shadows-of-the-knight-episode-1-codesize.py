p=lambda:map(int,input().split())
r,b=p()
l=t=0
p()
x,y=p()
while 1:
 d=input()
 if'U'in d:b=y;y=y+(t-y)//2
 elif'D'in d:t=y;y=y+(b-y)//2
 if'L'in d:r=x;x=x+(l-x)//2
 elif'R'in d:l=x;x=x+(r-x)//2
 print(x,y)