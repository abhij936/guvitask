a,b=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(len(l)) :
    for j in range(len(l)) :
        if (l[i]+l[j]==b) :
            count+=1
if (count>0) :
    print("yes")
else :
    print("no")
