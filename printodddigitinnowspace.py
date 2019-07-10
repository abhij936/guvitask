inp=input()
array=[]
if(inp.isdigit()==True):
    for i in inp:
        if(int(i)%2!=0):
            print(i, end=' ')
