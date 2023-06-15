r=input
w=int(r())
r()
m=r()
import re
while 1:l=r();print("".join(l[(ord(c)-65)*w:(ord(c)-64)*w]for c in re.sub(r'[^A-Z]','[',m.upper())))