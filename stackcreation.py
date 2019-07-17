class stack :
    def __init__(self,size=0):
        self.size=size
        self.list1=[]
        
    def add(self,data):
        if len(self.list1)>=self.size :
            print("stack is full")
            return
        self.list1.append(data)
        
    def remove(self) :
        if(len(self.list1)<=0):
            print("stack is empty")
            return
        self.list1.pop()
        
    def printStack(self):
        for ele in self.list1:
            print(ele)
            
a=stack(10)
a.add(1)
a.add(2)
a.remove()
a.printStack()
