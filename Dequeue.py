class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtLast(self, value):
        self.items.append(value)

    def deleteFromFirst(self):
        if(self.isEmpty()):
            print("Queue is empty")
        else:
            return self.items.pop(0)
        
    def insertAtFirst(self, value):
        self.items.insert(0, value)

    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Queue is empty")
        return self.items.pop()


dq = Deque()
dq.insertAtLast(10)
dq.insertAtFirst(20)
dq.insertAtLast(30)
dq.insertAtLast(40)
dq.insertAtFirst(50)

print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteFromFirst())
print(dq.deleteFromFirst())
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
