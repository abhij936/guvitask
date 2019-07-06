count=0
n,d = map(int, input().split())
l=list(map(int,input().split()))
for i in range(len(l)):
    if (l[i]==d):
        count+=1
print(count)
