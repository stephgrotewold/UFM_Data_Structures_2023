from queue import LinearQueue


# Queue instance
queue = LinearQueue(5)
print(queue)

# Enqueues
queue.enqueue('A')
print(queue)
queue.enqueue('B')
print(queue)
queue.enqueue('C')
print(queue)
queue.enqueue('D')
print(queue)


#search	
queue.search('C')

queue.enqueue('E')
print(queue)



queue.enqueue('F') # Queue Overflow
queue.enqueue('G') # Queue Overflow

print("Peeked:")	
queue.peek()




# Dequeues
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue() # Queue Underflow (2nd scenario)
queue.dequeue() # Queue Underflow (2nd scenario)

queue_2 = LinearQueue(5)
print(queue_2)
queue.dequeue() # Queue Underflow (1st scenario)
