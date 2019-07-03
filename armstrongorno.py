n=0
ans=0
no=int(input())
a=no
while ((a<10000) and (a!=0)) :
    a//=10
    n+=1
a=no
while((a<=10000) and (a!=0)) :
    r=a%10;
    ans+=pow(r,n)
    a//=10
    int(a)
if(ans==no) :
   print("yes")
else :
    print("no")
