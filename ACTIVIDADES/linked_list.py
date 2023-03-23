class Node:

    def __init__(self, data: str):
        self.data = data
        self.next = None

    
    def __repr__(self):
        return ' | Data: {} |'.format(self.data)
    


class LinkedList:

    def __init__(self):
        self.start = None
    
    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(node.data)

        nodes.append("NIL")
        return " --> " .join(nodes)

    def traverse(self):
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next
    
    def traverse_iter(self):
        for current_node in self:
            print(current_node)
    
    def insert_at_beginnig(self, new_node: Node):
        new_node.next = self.start
        self.start = new_node

    def insert_at_end(self, new_node: Node):
        if self.start is None:
            self.start = new_node
        else:
            for current_node in self:
                pass

            current_node.next = new_node

    def insert_before(self,reference_node: str, new_node: Node):
        if self.start is None:
            print('Emptyyy linked list')
            return
        
        if self.start.data == reference_node:
            return self.insert_at_beginnig(new_node)
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = new_node
                new_node.next = current_node
                return
            
            previous_node =  current_node
        
        print('Reference node {} not found in linked list...' .format(reference_node))
    
    def delete(self, reference_node: str):
        if self.start is None:
            print("Empty")
            return
        
        if self.start.data == reference_node:
            self.start = self.start.next
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = current_node.next
                return
            
            previous_node = current_node
        
        print('Reference node {} not found in linked list...' .format(reference_node))

    def search(self, x):
 
        current = self.start

        while current != None:
            if current.data == x:
                print('Si esta {}'.format(current))
                return True  
 
            current = current.next
        else:
            print('No se encontro')
            return False  
        