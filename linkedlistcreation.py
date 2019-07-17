class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
    def insert(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

if __name__=='__main__':
    obj=LinkedList()
    obj.head=Node(1)
    second=Node(2)
    third=Node(3)
    obj.head.next=second
    second.next=third
    obj.insert(4)
    obj.printList()
