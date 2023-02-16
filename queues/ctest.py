from cqueue import TheCircularQueue

# Queue instance
queue = TheCircularQueue(5)
print(queue)
queue.printCQueue()

# Enqueues
queue.enqueue('A')
print(queue)
queue.printCQueue()
queue.enqueue('B')
print(queue)
queue.printCQueue()
queue.enqueue('C')
print(queue)
queue.printCQueue()
queue.enqueue('D')
print(queue)
queue.printCQueue()
queue.enqueue('E')
print(queue)
queue.printCQueue()

queue.search('D')

print("Peeked:")	
queue.peek()

queue.enqueue('F') # Queue Overflow
queue.enqueue('G') # Queue Overflow
queue.printCQueue()

# Dequeues
queue.dequeue()
print(queue)
queue.printCQueue()

queue.enqueue('S') # Queue startover
print(queue)
queue.printCQueue()


queue.dequeue()
print(queue)
queue.printCQueue()
queue.dequeue()
print(queue)
queue.printCQueue()
queue.dequeue()
print(queue)
queue.printCQueue()




print("Peeked:")	
queue.peek()

queue.dequeue()
print(queue)
queue.printCQueue()
queue.dequeue() # Queue Underflow (2nd scenario)
print(queue)


queue_2 = TheCircularQueue(5)
print(queue_2)
queue.dequeue() # Queue Underflow (1st scenario)



