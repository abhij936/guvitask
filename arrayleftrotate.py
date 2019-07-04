n,d=map(int,input().split())
arr=list(map(int,input("").split()))
size=len(arr)

def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n)
        
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i + 1] 
    arr[n-1] = temp
    
def printArray(arr, size): 
    for i in range(size): 
        print (arr[i], end =" ")
        
leftRotate(arr, d, n)
printArray(arr, size)
