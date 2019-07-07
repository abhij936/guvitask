num=int(input())
if ((num>1) and (num<=1000)) :
    for x in range(2,num) :
        if (num%x==0) :
            print("no")
            break
    else:
        print("yes")
else:
     print("no")
