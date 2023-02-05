# This priority queue is implemented using a linked list
# this is to reduce the time taken to insert into the middle of a list
# e.g.
# [{a:5},{b:3},{c:1},None,None,None,None,None,None,None]
# enqueue({d:2})
# [{a:5},{d:3},{b:2},{c:1},None,None,None,None,None,None]
# this requires shifting all the elements past priority 2 to the right

from Color import Colors


class PQNode:
    def __init__(self, data, priority):
        self.__data = data
        self.__priority = priority
        self.__Next: PQNode = None

    def getNext(self):
        return self.__Next

    def getData(self):
        return self.__data

    def getPriority(self):
        return self.__priority

    def setNext(self, Next):
        self.__Next = Next

    def setData(self, data):
        self.__data = data

    def setPriority(self, priority):
        self.__priority = priority


class PriorityQueue:
    def __init__(self):
        self.head: PQNode = None
        self.tail: PQNode = None

    def is_Empty(self):
        return self.head is None

    def enqueue(self, data, priority):
        newNode = PQNode(data, priority)

        if self.is_Empty():
            self.head = newNode
            self.tail = newNode
        else:
            if priority > self.head.getPriority():
                newNode.setNext(self.head)
                self.head = newNode
            elif priority <= self.tail.getPriority():
                self.tail.setNext(newNode)
                self.tail = newNode
            else:
                current = self.head

                while current.getNext().getPriority() >= priority:
                    current = current.getNext()

                newNode.setNext(current.getNext())
                current.setNext(newNode)

    def dequeue(self):
        if self.is_Empty():
            print("Queue is empty\n")
            outValue = None
        else:
            outValue = self.head.getData()
            self.head = self.head.getNext()

        return outValue


class VisualPriorityQueue:
    def __init__(self):
        self.head: PQNode = None
        self.tail: PQNode = None

    def is_Empty(self):
        return self.head is None

    def enqueue(self, data, priority):
        newNode = PQNode(data, priority)

        print(Colors.BLUE + "Enqueueing: " + data + " at priority: " + str(priority) + Colors.ENDC)
        print("before: ")
        self.print()

        if self.is_Empty():
            self.head = newNode
            self.tail = newNode
        else:
            if priority > self.head.getPriority():
                newNode.setNext(self.head)
                self.head = newNode
            elif priority <= self.tail.getPriority():
                self.tail.setNext(newNode)
                self.tail = newNode
            else:
                current = self.head

                while current.getNext().getPriority() >= priority:
                    current = current.getNext()

                newNode.setNext(current.getNext())
                current.setNext(newNode)

        print("\nafter: ")
        self.print()
        print("\n\n")

    def dequeue(self):
        value = self.head.getData() if self.head is not None else None
        priority = self.head.getPriority() if self.head is not None else None
        print(Colors.CYAN + "Dequeueing the value " + str(value) + " at priority: " + str(priority) + Colors.ENDC)
        print("before: ")
        self.print()

        if self.is_Empty():
            print("Queue is empty\n")
            outValue = None
        else:
            outValue = self.head.getData()
            self.head = self.head.getNext()

        print("\nafter: ")
        self.print()
        print("\n\n")

        return outValue

    def peek(self):
        value = self.head.getData() if self.head is not None else None
        priority = self.head.getPriority() if self.head is not None else None
        print("Peeking the value " + str(value) + " at priority: " + str(priority))
        print("before: ")
        self.print()

        print("\nafter: ")
        self.print()
        print("\n\n")

        return value

    def print(self):
        current = self.head
        print(" v--Head" if current is not None else "Queue is empty")
        while current is not None:
            print("{" + current.getData() + " priority: " + str(current.getPriority()) + "}" + (
                " -> " if current.getNext() is not None else "\n"), end="")
            current = current.getNext()
