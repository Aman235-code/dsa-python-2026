class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None 
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,value):
        temp = Node(value)
        if(self.head is None):
            self.head = temp 
            return
        tail = self.head 
        while tail.next != None:
            tail = tail.next
        tail.next = temp 
        temp.prev = tail

    def insert_at_beginning(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp 
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_at_middle(self, value, x):
        t = self.head
        temp = Node(value)
        while t.next!=None:
            if(t.data == x):
                break 
            else: 
                t = t.next
        temp.next = t.next
        t.next.prev = temp
        t.next = temp 
        temp.prev = t

    def printDiublyLL(self):
        t = self.head
        while(t.next!=None):
            print(t.data, end=" ")
            t = t.next
        print(t.data, end=" ")

    def deletionDLL(self, value):
        if(self.head == None):
            print("LL is empty")
            return
        
        t = self.head
        if(t.data == value):
            self.head = t.next
            self.head.prev = None
            return

        while(t.next!=None):
            if(t.data == value):
                t.prev.next = t.next 
                t.next.prev = t.prev
                return
            else:
                t = t.next
            
        if(t.data == value):
            t.prev.next= None


obj = DoublyLinkedList()

obj.insert_at_end(1)
obj.insert_at_end(5)
obj.insert_at_end(10)

obj.insert_at_beginning(20)
obj.insert_at_beginning(30)

obj.insert_at_middle(50, 20)
obj.deletionDLL(1)

obj.printDiublyLL()
        