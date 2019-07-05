x=0
n=int(input())
l=list(map(int,input().split()))
for i in range(n) :
    x+=l[i]
a=x/n
print(int(a))
