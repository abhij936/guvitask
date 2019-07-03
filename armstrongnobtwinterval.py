p,q=map(int,input().split())
for x in range(p,q) :
   n=0
   ans=0
   a=x
   while ((a<10000) and (a!=0)) :
       a//=10
       n+=1
   a=x
   while((a<=10000) and (a!=0)) :
       r=a%10;
       ans+=pow(r,n)
       a//=10
       int(a)
   if(ans==x) :
       print(x)
