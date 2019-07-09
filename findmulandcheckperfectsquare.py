import math
a,b=map(int,input().split())
c=a*b
d=math.sqrt(c)
if (int(d)==d) :
    print("yes")
else :
    print("no")
