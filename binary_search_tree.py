class Node:
    """
    A class representing a node in a binary search tree.
    
    Attributes
    ----------
    data : int
        The value stored in the node.
    left_child : Node
        The left child of the node.
    right_child : Node
        The right child of the node.
    """

    def __init__(self, data: int) -> None:
        """
        Constructs a new Node instance.
        
        Parameters
        ----------
        data : int
            The value to be stored in the node.
        """
        self.data = data
        self.left_child = None
        self.right_child = None
        pass

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.
        
        Returns
        -------
        str
            A string representation of the node, which is the value stored in the node.
        """
        return'({})'.format(self.data)


class BinarySearchTree:
    """
    A class representing a binary search tree.
    """
    def __init__(self):
        """
        Constructs a new BinarySearchTree instance.
        """
        self.root = None
    
    def insert(self, value: int):
        """
        Inserts a value into the binary search tree.
        
        Parameters
        ----------
        value : int
            The value to be inserted.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value: int, subtree: Node):
        """
        Inserts a value into the binary search tree recursively.
        
        Parameters
        ----------
        value : int
            The value to be inserted.
        subtree : Node
            The root of the subtree being processed.
        """

        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else: 
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)
        
        else:
            print('El valor ya existe en el arbol')

    def traverse(self, subtree: Node):
        """
        Traverses the binary search tree in-order and prints each node value.
        
        Parameters
        ----------
        subtree : Node
            The root of the subtree being processed.
        """
        print(subtree)
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)
        
        if subtree.right_child is not None:
            self.traverse(subtree.right_child)

    def search(self, key: int) -> bool:
        """
        Searches the binary search tree for a specific value.
        
        Parameters
        ----------
        key : int
            The value to search for.
        
        Returns
        -------
        bool
            True if the value is found, False otherwise.
        """

        if self.root is None:
            return False
        
        else:
            return self._search(key, self.root)
    
    def _search(self, key: int, subtreee: Node) -> bool:
        """
        Searches a subtree of the binary search tree for a specific value recursively.
        
        Parameters
        ----------
        key : int
            The value to search for.
        subtree : Node
            The root of the subtree being processed.
        
        Returns
        -------
        bool
            True if the value is found, False otherwise.
        """

        if key == subtreee.data:
            return True
        
        elif(key < subtreee.data) and (subtreee.left_child is not None):
            return self._search(key, subtreee.left_child)
        
        elif(key > subtreee.data) and (subtreee.right_child is not None):
            return self._search(key, subtreee.right_child)
        
        else:
            return False
        
    
    #estos sirven para el delete
    def find_min(self, subtree: Node) -> int:
        """
        Finds and returns the minimum value in the subtree rooted at the given node.

        Args:
        - subtree (Node): The root node of the subtree to search.

        Returns:
        - The node with the minimum value in the subtree.
        """

        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree
    
    def find_max(self, subtree: Node) -> int:
        """
        Finds and returns the maximum value in the subtree rooted at the given node.

        Args:
        - subtree (Node): The root node of the subtree to search.

        Returns:
        - The node with the maximum value in the subtree.
        """
        while subtree.right_child is not None:
            subtree = subtree.right_child
        
        return subtree

    def delete(self, value: int) -> None:
        """
        Deletes the node with the given value from the tree.

        Args:
        - value (int): The value to delete from the tree.

        Returns:
        - None.
        """
        if self.root is None:
            return
        
        self.root = self._delete(value, self.root)
    
    def _delete(self, value: int, subtree: Node) -> Node:
        """
        Deletes the node with the given value from the subtree rooted at the given node.

        Args:
        - value (int): The value to delete from the subtree.
        - subtree (Node): The root node of the subtree to delete from.

        Returns:
        - The new root node of the subtree after deleting the node.
        """
        if subtree is None:
            return subtree
        
        if value < subtree.data:
            subtree.left_child = self._delete(value, subtree.left_child)
        elif value > subtree.data:
            subtree.right_child = self._delete(value, subtree.right_child)
        else:
            if subtree.left_child is None:
                return subtree.right_child
            elif subtree.right_child is None:
                return subtree.left_child
            
            temp = self.find_min(subtree.right_child)
            subtree.data = temp.data
            subtree.right_child = self._delete(temp.data, subtree.right_child)
        
        return subtree
        


