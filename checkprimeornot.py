num1=int(input())
if ((num1>1) and (num1<=1000)) :
    for x in range(2,num1) :
        if (num1%x==0) :
            print("no")
            break
    else:
        print("yes")
else:
     print("no")
