class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point to old head
        self.head = new_node       # Update head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

# Usage
ll = LinkedList()
ll.insert_at_start('Gospel')
ll.insert_at_start('RnB')
ll.display()
