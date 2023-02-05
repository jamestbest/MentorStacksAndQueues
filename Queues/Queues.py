from Color import Colors


class Queue:
    def __init__(self):
        self.MAX_SIZE = 10
        self.arr = [None] * self.MAX_SIZE
        self.head = 0  # points to the first element
        self.tail = -1  # points to the last element

    def is_Empty(self):
        return self.head > self.tail

    def is_Full(self):
        return self.tail == self.MAX_SIZE - 1

    def enqueue(self, data):
        if self.is_Full():
            print("Queue is full\n")
            return
        else:
            self.tail += 1
            self.arr[self.tail] = data

    def dequeue(self):
        if self.is_Empty():
            print("Queue is empty\n")
            outValue = None
        else:
            outValue = self.arr[self.head]
            self.head += 1

        return outValue

    def peek(self):
        if self.is_Empty():
            print("Queue is empty\n")
            outValue = None
        else:
            outValue = self.arr[self.head]

        return outValue

    def print(self):
        print(self.arr)


class VisualQueue:
    def __init__(self, isCircular=False):
        self.MAX_SIZE = 10
        self.arr = [None] * self.MAX_SIZE
        self.head = 0
        self.tail = -1

        self.isCircular = isCircular

    def is_Empty(self):
        return self.head > self.tail

    def is_Full(self):
        return self.tail == self.MAX_SIZE - 1

    def enqueue(self, data):
        print(Colors.BLUE + "Enqueueing the value: " + str(data) + Colors.ENDC)
        print("before: ")
        self.print()

        if self.is_Full():
            print(Colors.RED + "Queue is full\n" + Colors.ENDC)
            return
        else:
            self.tail += 1
            self.arr[self.tail] = data

        print("\nafter: ")
        self.print()
        print("\n\n")

    def dequeue(self):
        value = self.arr[self.head] if not self.is_Empty() else None
        print(Colors.CYAN + "Dequeueing the value: " + str(value) + Colors.ENDC)
        print("before: ")
        self.print()

        if self.is_Empty():
            print(Colors.RED + "Queue is empty\n" + Colors.ENDC)
            outValue = None
        else:
            outValue = self.arr[self.head]
            self.head += 1

        print("\nafter: ")
        self.print()
        print("\n\n")

        return outValue

    def peek(self):
        print(Colors.GREEN + "Peeking the value: " + str(self.arr[self.head]) + Colors.ENDC)
        print("before: ")
        self.print()

        if self.is_Empty():
            print("Queue is empty\n")
            outValue = None
        else:
            outValue = self.arr[self.head]

        print("\nafter: ")
        self.print()
        print("\n\n")
        return outValue

    def getPointerPositionInString(self, pointerPosition):
        if pointerPosition <= -1:
            return 0

        pos = 1  # [
        for i in range(pointerPosition):
            pos += 4  # '',
            if self.arr[i] is not None:
                pos += len(self.arr[i])

        return pos

    def getPointerStrings(self):
        out = ""

        out += "-" * self.getPointerPositionInString(self.head) + ("^H" if self.head != -1 else "") + "\n"

        out += "-" * self.getPointerPositionInString(self.tail) + ("^T" if self.tail != -1 else "")

        return out

    def print(self):
        print(self.arr)
        print(self.getPointerStrings())
        print("value of the head pointer: " + str(self.head))
        print("value of the tail pointer: " + str(self.tail))
