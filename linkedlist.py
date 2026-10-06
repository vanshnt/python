class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
list = LinkedList()
t1 = Node(10)
t2 = Node(20)
t3 = Node(30)

list.append(t1)
list.append(t2)
list.append(t3)
list.append(Node(40))
list.print()