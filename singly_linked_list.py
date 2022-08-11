class Node:

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    def __repr__(self):
          return "<Node data: %s>" % self.data


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.count = 0
    def is_empty(self):
        return self.head is None
            
    def size(self):
        current = self.head
        while current:
            self.count +=1
            current = current.next_node
        return self.count
        
    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        if index == 0:
            return self.add(data)
        
        if index > 0:
            current = self.head
            new_node = Node(data)
            position = index
            
            while position > 1:
                current = current.next_node
                position -=1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node
    def remove(self, key):
        current = self.head
        found = False
        previous = None

        while current and not found:
            if current.data == key and current is self.head:
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
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return "-> ".join(nodes)

        