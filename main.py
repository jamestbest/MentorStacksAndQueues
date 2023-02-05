import random

from Stacks import VisualStack, Stack
from Queues import VisualQueue, Queue
from CircularQueues import VisualCircularQueue, CircularQueue
from PriorityQueues import VisualPriorityQueue, PriorityQueue
import StackFrames
from Color import Colors

myStack = VisualStack()
myQueue = VisualQueue()
myCircularQueue = VisualCircularQueue()
myPriorityQueue = VisualPriorityQueue()


def StackExample():
    print(Colors.UNDERLINE + "Stacks" + Colors.ENDC)
    myStack.push("a")
    myStack.push("b")

    myStack.pop()
    myStack.pop()
    myStack.pop()

    myStack.push("c")
    myStack.push("d")

    myStack.peek()
    myStack.pop()
    myStack.pop()
    myStack.peek()


def fillStack(stack):
    for i in range(stack.MAX_SIZE):
        stack.push(chr(65 + i))


def emptyStack(stack):
    fillStack(stack)
    for i in range(stack.MAX_SIZE):
        stack.pop()


def StackOverflow():
    print(Colors.UNDERLINE + "Stack Overflow" + Colors.ENDC)
    fillStack(myStack)
    myStack.push("z")


def StackUnderflow():
    print(Colors.UNDERLINE + "Stack Underflow" + Colors.ENDC)
    emptyStack(myStack)
    myStack.pop()


def QueueExample():
    print(Colors.UNDERLINE + "Queues" + Colors.ENDC)
    myQueue.enqueue("a")
    myQueue.enqueue("b")
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.enqueue("c")
    myQueue.enqueue("d")


def fillQueue(queue, offset=0):
    for i in range(queue.MAX_SIZE):
        queue.enqueue(chr(65 + i + offset))


def emptyQueue(queue):
    fillQueue(queue)
    for i in range(queue.MAX_SIZE):
        queue.dequeue()


def CircularQueueExample():
    print(Colors.UNDERLINE + "Circular Queues" + Colors.ENDC)
    fillQueue(myCircularQueue)

    for i in range(myCircularQueue.MAX_SIZE // 2):
        myCircularQueue.dequeue()

    fillQueue(myCircularQueue, offset=12)


def PriorityQueueExample():
    myPriorityQueue.enqueue("a", 1)
    myPriorityQueue.enqueue("b", 2)
    myPriorityQueue.enqueue("c", 3)
    myPriorityQueue.enqueue("d", 3)
    myPriorityQueue.enqueue("e", 2)

    emptyPriorityQueue(myPriorityQueue)


def fillPriorityQueue(queue, offset=0):
    for i in range(10):
        queue.enqueue(chr(65 + i + offset), random.randint(1, 10))


def emptyPriorityQueue(queue):
    fillPriorityQueue(queue)
    while not queue.is_Empty():
        queue.dequeue()


if __name__ == '__main__':
    # StackExample()
    # StackOverflow()
    # StackUnderflow()

    # QueueExample()

    # fillQueue(myQueue)
    # emptyQueue(myQueue)

    # CircularQueueExample()

    # PriorityQueueExample()

    StackFrames.main()

    print("end")
