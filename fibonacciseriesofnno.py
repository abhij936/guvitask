inp=int(input())
n1=1
n2=1
count=0
if (inp=='0') :
    print("0")
while (count<inp) :
    print(n1, end=' ')
    n3=n1+n2
    n1=n2
    n2=n3
    count+=1
