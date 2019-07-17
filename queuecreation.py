class queue:
    def __init__(self,size=0):
        self.size=size
        self.list1=[]
        
    def enqueue(self,data):
        if len(self.list1)>=self.size :
            print("queue is full")
            return
        self.list1.append(data)
    
    def dequeue(self):
        if len(self.list1)<=0 :
            print("queue is empty")
            return
        self.list1.pop(0)
        
    def printQueue(self):
        print(*self.list1)
    
a=queue(2)
a.enqueue(1)
a.enqueue(2)
a.enqueue(2)
a.dequeue()
a.printQueue()
