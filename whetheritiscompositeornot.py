sur=int(input())
if(sur>1):
    for i in range(2,sur):
        if(sur%i==0):
            print("yes")
            break
    else:
        print("no")
