from binary_tree import Node, BinaryTree

#nodos
node_a = Node('A')
print(node_a)
node_b = Node('B')
print(node_b)
node_c = Node('C')
print(node_c)

print('----------------------------------')

#tree
tree = BinaryTree()


#add node to rote
tree.root = node_a

# B left child de A
node_a.left_child = node_b

# C right child de B
node_b.right_child = node_c

print(tree.root)
print(tree.root.left_child)
print(tree.root.left_child.right_child)