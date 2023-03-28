class Node:

    def __init__(self, data:str):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def __repr__(self) -> str:
        return '({})'.format(self.data)
    
class BinaryTree:

    def __init__(self):
        self.root = None

    