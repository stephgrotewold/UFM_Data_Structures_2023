from linked_list import Node , LinkedList

# nodes instantiation
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')


# node in memory
print(node_a)
print(id(node_a))


# create LL
ll = LinkedList()
print(ll)

# insert at beginning
ll.insert_at_beginnig(node_c)
print(ll)
ll.insert_at_beginnig(node_b)
print(ll)
ll.insert_at_beginnig(node_a)
print(ll)
ll.insert_at_beginnig(node_d)
print(ll)

#insert at end
ll.insert_at_end(node_e)
print(ll)

#insert before
ll.insert_before('A', node_f)
print(ll)

node_g = Node('G')
ll.insert_before('D', node_g)
print(ll)

node_h = Node('H')
ll.insert_before('E', node_h)
print(ll)


ll.search('B')
ll.search('Z')