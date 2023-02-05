import Queues
from Color import Colors


class CircularQueue:
    def __init__(self):
        self.MAX_SIZE = 10
        self.arr = [None] * self.MAX_SIZE

        self.head = -1
        self.tail = -1

    def is_Empty(self):
        if self.head == -1:
            return True
        else:
            return False

    def is_Full(self):
        if (self.tail + 1) % self.MAX_SIZE == self.head:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.is_Full():
            print("Queue is full\n")
            return
        else:
            self.tail = (self.tail + 1) % self.MAX_SIZE
            self.arr[self.tail] = data

            if self.head == -1:
                self.head = 0

    def dequeue(self):
        if self.is_Empty():
            print("Queue is empty\n")
            outValue = None

        else:
            outValue = self.arr[self.head]

            if self.head == self.tail:  # queue is empty
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1) % self.MAX_SIZE

        return outValue

    def peek(self):
        if self.is_Empty():
            print("Queue is empty\n")
            outValue = None
        else:
            outValue = self.arr[self.head]

        return outValue


class VisualCircularQueue(Queues.VisualQueue):
    def __init__(self):
        super().__init__()
        self.MAX_SIZE = 10
        self.arr = [None] * self.MAX_SIZE

        self.head = -1
        self.tail = -1

    def is_Empty(self):
        return self.head == -1

    def is_Full(self):
        return (self.tail + 1) % self.MAX_SIZE == self.head

    def enqueue(self, data):
        print(Colors.BLUE + "Enqueueing the value: " + str(data) + Colors.ENDC)
        print("before: ")
        self.print()

        if self.is_Full():
            print(Colors.RED + "Queue is full\n" + Colors.ENDC)
            return
        else:
            self.tail = (self.tail + 1) % self.MAX_SIZE
            self.arr[self.tail] = data

            if self.head == -1:
                self.head = 0

        print("\nafter: ")
        self.print()
        print("\n\n")

    def dequeue(self):
        print(Colors.CYAN + "Dequeueing the value: " + str(self.arr[self.head]) + Colors.ENDC)
        print("before: ")
        self.print()

        if self.is_Empty():
            print(Colors.RED + "Queue is empty\n" + Colors.ENDC)
            outValue = None

        else:
            outValue = self.arr[self.head]

            if self.head == self.tail:  # queue is empty
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1) % self.MAX_SIZE

        print("\nafter: ")
        self.print()
        print("\n\n")

        return outValue

    def peek(self):
        print(Colors.GREEN + "Peeking the value: " + str(self.arr[self.head]) + Colors.ENDC)
        print("before: ")
        self.print()

        if self.is_Empty():
            print(Colors.RED + "Queue is empty\n" + Colors.ENDC)
            outValue = None
        else:
            outValue = self.arr[self.head]

        print("\nafter: ")
        self.print()
        print("\n\n")
        return outValue
