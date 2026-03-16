class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None
    
class LinkedList:
    def __init__(self): # Removed the 'head' parameter here
        self.head = None

    def insert_at_End(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # Start from the head to find the end
        current = self.head 
        while current.Next: # Fixed: current was undefined
            current = current.Next

        # Link the last node to the new node
        current.Next = new_node 

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.Next
        print("None")

    
    def insert_at_Beg(self,data):
        new_node = Node(data)
        new_node.Next = self.head
        self.head = new_node


# ===================================
LL = LinkedList() 
LL.insert_at_End(5)
LL.insert_at_End(15)
LL.insert_at_Beg(3)

LL.display()
