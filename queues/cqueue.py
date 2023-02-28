class TheCircularQueue():
    def __init__(self, size:int) -> None:
        self.max = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    #def __repr__(self) -> None:
       # return 'Current queue: {} | Front: {} | Rear: {}'.format(self.queue, self.front, self.rear)
    
    def enqueue(self,value: str)-> None:
        if((self.rear +1) % self.max == self.front):
            print("This thing is full bro\n")
        
        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        
        else:
            self.rear = (self.rear + 1)%self.max
            self.queue[self.rear] = value
        
        self.queue[self.rear] = value
    
    def dequeue(self) -> str:
        if(self.front == -1):
            print('This thing is hella empty')
        
        elif(self.front == self.rear):
            piv = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return piv
        
        else: 
            piv = self.queue[self.front]
            self.front = (self.front + 1)% self.max
            return piv
    
    def peek(self):
        print(self.queue[self.front])

    def search(self, val: str) -> None:

        while self.front <= self.rear:

            if self.queue[self.front] == val:
                print("Esta ubicado en: ", self.front)
                return val
            self.front += 1
        print("No se encuentra lol")   
        self.front = 0
    
    def printCQueue(self):
        if(self.front == -1):
            print("This b is emptyyyy")

        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.max):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
    