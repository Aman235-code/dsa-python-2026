class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node 

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def insert_after_value(self, target, value):
        new_node = Node(target)
        current = self.head

        while current.next is not None:
            if current.data == value:
                new_node.next = current.next
                current.next = new_node
                
            current = current.next

    def delete_by_value(self, value):
        current = self.head

        if current and current.data == value:
            self.head = current.next
            return

        previous = None
        while current and current.data != value:
            previous = current
            current = current.next

        if current is None:
            return

        previous.next = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next



obj = SinglyLinkedList()
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.insert_at_end(50)

obj.insert_at_start(10)
obj.insert_at_start(20)

obj.insert_after_value(40, 20)

obj.delete_by_value(50)

obj.print_list()