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

