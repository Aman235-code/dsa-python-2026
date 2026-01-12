class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size 
        self.front = self.rear = -1 

    def insert(self, value):
        if ( (self.rear + 1) % self.size) == self.front:
            print("Queue is full")
        
        elif self.rear == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value

        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value

    def remove(self):
        if(self.front == -1):
            print("Queue is Empty")

        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1

        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size

cq = CircularQueue(5)
cq.insert(10)
cq.insert(20)
cq.insert(30)
cq.insert(40)
cq.insert(50)
# cq.insert(60)

cq.remove()
cq.insert(60)
# cq.insert(70)
cq.remove()
cq.remove()
cq.remove()
cq.remove()
cq.remove()

        