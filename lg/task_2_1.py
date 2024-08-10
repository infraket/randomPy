
class FifoBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start = 0
        self.end = 0
        self.length = 0

    def enqueue(self, item):
        if self.length == self.size:

            self.dequeue()

        self.buffer[self.end] = item
        self.end = (self.end + 1) % self.size
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        item = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.size
        self.length -= 1

        return item

    def peek(self):
        if self.length == 0:
            return None

        return self.buffer[self.start]

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.size

# код реализует циклический буфер Fifo с фиксированным размером.


