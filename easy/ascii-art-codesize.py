w,h,m,*a=open(0)
w,h=int(w),int(h)
import re
for i in range(h):print("".join(a[i][(ord(c)-65)*w:(ord(c)-64)*w]for c in re.sub(r'[^A-Z]','[',m.upper())[:-1]))