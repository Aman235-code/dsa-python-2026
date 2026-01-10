class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next 

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head 

    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head != None): # atleas 1 LL is present
            t1 = self.head # t1 points to first node
            while(t1.next!=None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp 

    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def printLL(self):
        t1 = self.head
        while(t1.next!=None):
            print(t1.data, end=" ")
            t1 = t1.next 
        print(t1.data, end=" ")

    def insertInMiddle(self, value, x): # x referes to the data in ll we insert value after x
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteLL(self, value):
        t1 = self.head
        prev = t1 
        if(t1.data == value):
            self.head = t1.next

        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1 
                t1 = t1.next

        if(t1.data == value):
            prev.next = None

obj = SinglyLinkedList()
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(50)

obj.insertAtBeg(10)
obj.insertAtBeg(20)

obj.insertInMiddle(40, 20)

obj.deleteLL(50)

obj.printLL()
        
        