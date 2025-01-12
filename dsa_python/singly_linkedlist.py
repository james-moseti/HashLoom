# jemo_tech@2025
# Implementation of a singly linked list

class Node:
    """
    An object for storing a single node of a linked list. 
    Has two attributes - the data and the next_node: reference to next node in the linked list 
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "<Node data:  %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns teh number of nodes in the linked list
        Takes O(n)
        """
        current = self.head
        count = 0
        
        while current != None:
            count += 1
            current = current.next_node
            
        return count
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self, key):
        """
        Search for the first node containing the key
        Return the node if found or `None` if not found
        Running time O(n)
        """
        current = self.head
        
        while current != None:
            if current.data == key:
                return  current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Insert a new node at the index position.
        Insert running time O(1); Finding node takes O(n).
        Overall running time O(n).
        """
        if index < 0:
            raise IndexError("Index must be a non-negative integer")
        
        if index == 0:
            self.add(data)
            return

        if self.head is None:
            raise IndexError("Cannot insert at index > 0 in an empty list")

        new = Node(data)
        current = self.head
        position = index

        while position > 1 and current is not None:
            current = current.next_node
            position -= 1

        if current is None:
            raise IndexError("Index out of bounds")

        prev_node = current
        next_node = current.next_node

        prev_node.next_node = new
        new.next_node = next_node
        
    def remove(self, key):
        """
        Removes node containing data that matches the key
        Returns the node removed or None if key doesn't exist
        Running time O(n)
        """
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current

        
    def __repr__(self):
        """
        Return a string representation of the linked list
        Running time O(n)
        """
        
        nodes = []
        current = self.head
        
        while current != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
                
            current= current.next_node
        return '-> '.join(nodes)