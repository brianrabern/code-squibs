class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.head = 0
        self.tail = 0
        self.buffer = [None]*size
        self.length = 0

    def enqueue(self, value):
        self.buffer[self.tail] = value
        self.tail += 1
        self.length += 1
        if self.tail >= self.size:
            self.tail = 0

    def dequeue(self):
        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head += 1
        self.length -= 1
        if self.head >= self.size:
            self.head = 0
        return value


m = CircularQueue(3)
m.enqueue(6)
m.dequeue()
m.enqueue(8)
m.dequeue()
m.enqueue(2)


print(m.buffer[0])
print(m.buffer[1])
print(m.buffer[2])
