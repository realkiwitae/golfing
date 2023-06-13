X,Y,x,y=map(int,input().split())
while 1:w,h=X-x,Y-y;print('N'*(h<0)+'S'*(h>0)+'W'*(w<0)+'E'*(w>0));x+=w>0;y+=h>0