a,b=map(int,input().split())
for m in range(a+1,b) :
   for x in range(2,m) :
       if (m%x==0) :
           break
   else:
       print(m, end=' ')
