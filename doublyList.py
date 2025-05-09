class Node:
    def __init__(self, data):
        self.data = data #Stores the data
        self.next = None #Points to the next node
        self.prev = None  # Points to the previous node

class LinkedList:
    def __init__(self):
        self.head = None #Starts off the list

    def insert_at_start(self, data):
        new_node = Node(data) #Creates a new node
        new_node.next = self.head# Point to current head(if any)
        if self.head:
            self.head.prev = new_node  # Set previous of old head
        self.head = new_node      # Update head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

# Usage
ll = LinkedList()
ll.insert_at_start('gospel')
ll.insert_at_start('RnB')
ll.display()
