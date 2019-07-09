a=int(input())
l,r=map(int,input().split())
for i in range(l+1,r+1) :
    if (a==i) :
        print("yes")
        break
else :
    print("no")
