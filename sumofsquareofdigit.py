no=int(input())
result=0
while ((no!=0) and (no<=1000000000000000000)) :
    r=no%10
    result+=pow(r,2)
    no//=10
print(result)
