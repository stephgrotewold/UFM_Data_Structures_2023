from data_persistence import pickle_object
from linked_list import Node
from memory_profiler import *
from stack import Stack
import sys

sys.setrecursionlimit(100000)

@profile
def stackity(n :int) -> Stack:
    stck = Stack(n)
    node = Node('nodes')

    for _ in range(n):
        stck.push(node)
    return stck

stack_2 = stackity(100000)
pickle_object(stack_2, './ACTIVIDADES/stackitys')
