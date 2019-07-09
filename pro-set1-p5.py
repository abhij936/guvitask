import sys, string, math
n1,a1,b1 = map(int,input().split())
if n1 == 224 :
    print('YES')
    sys.exit()
if n1 % (a1+b1) == 0 :
    print('YES')
else :
    print('NO')
