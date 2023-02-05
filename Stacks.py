from Color import Colors


class Stack:
    def __init__(self):
        self.MAX_SIZE = 10
        self.arr = [None] * self.MAX_SIZE
        self.stackPointer = 0

    def is_Full(self):
        if self.stackPointer == self.MAX_SIZE - 1:
            return True
        else:
            return False

    def is_Empty(self):
        if self.stackPointer == 0:
            return True
        else:
            return False

    def push(self, data):
        if self.is_Full():
            print("Stack is full\n")
            return
        else:
            self.stackPointer += 1
            self.arr[self.stackPointer] = data

    def pop(self):
        if self.is_Empty():
            print("Queue is empty\n")
            outValue = None
        else:
            outValue = self.arr[self.stackPointer]
            self.stackPointer -= 1

        return outValue

    def peek(self):
        if self.is_Empty():
            print("Queue is empty\n")
            outValue = None
        else:
            outValue = self.arr[self.stackPointer]

        return outValue


class VisualStack:
    def __init__(self, printVertical=False):
        self.MAX_SIZE = 10
        self.arr = [None] * self.MAX_SIZE
        self.stackPointer = -1
        self.printVertical = printVertical

    def is_Full(self):
        return self.stackPointer == self.MAX_SIZE - 1

    def is_Empty(self):
        return self.stackPointer == -1

    def push(self, data):
        print(Colors.BLUE + "pushing the value '" + str(data) + "' into the stack" + Colors.ENDC)
        print("before pushing")
        self.print()

        if self.is_Full():
            print(Colors.RED + "Stack is full, cannot push\n" + Colors.ENDC)
        else:
            self.stackPointer += 1
            self.arr[self.stackPointer] = data

        print("\nafter pushing")
        self.print()
        print("\n\n")

    def pop(self):
        print(Colors.CYAN + "popping the value '" + str(self.arr[self.stackPointer]) + "' from the stack" + Colors.ENDC)
        print("before popping")
        self.print()

        if self.is_Empty():
            print(Colors.RED + "Stack is empty, cannot pop\n" + Colors.ENDC)
            outValue = None
        else:
            outValue = self.arr[self.stackPointer]
            self.stackPointer -= 1

        print("\nafter popping")
        self.print()
        print("\n\n")
        return outValue

    def peek(self):
        print(
            Colors.GREEN + "peeking the value '" + str(self.arr[self.stackPointer]) + "' from the stack" + Colors.ENDC)
        print("before peeking")
        self.print()

        if self.is_Empty():
            print(Colors.RED + "Stack is empty, cannot peek\n" + Colors.ENDC)
            outValue = None
        else:
            outValue = self.arr[self.stackPointer]

        print("\nafter peeking")
        self.print()
        print("\n\n")
        return outValue

    def getPointerPositionInString(self):
        if self.is_Empty():
            return 0

        pos = 1  # [
        for i in range(self.stackPointer):
            pos += 4  # '',
            if self.arr[i] is not None:
                pos += len(self.arr[i])

        return pos

    def getPointerString(self):
        return "-" * self.getPointerPositionInString() + ("^" if not self.is_Empty() else "")

    def printArr(self):
        out = "["
        for i in range(self.MAX_SIZE - 1):
            out += "'" + str(self.arr[i]) + "', "

        out += "'" + str(self.arr[self.MAX_SIZE - 1]) + "']"
        print(out)

    def print(self):
        if not self.printVertical:
            self.printArr()
            print(self.getPointerString())
            print("value of the pointer: " + str(self.stackPointer))
        else:
            values = []
            maxLen = 0
            for i in range(self.MAX_SIZE):
                value = str(self.arr[i])
                values.append("'" + value + "'")
                if len(value) > maxLen:
                    maxLen = len(value)

            out = ""

            pointerPos = self.getPointerPositionInString()

            for i in range(self.MAX_SIZE - 1, -1, -1):
                out += "|" + values[i].center(maxLen + 4) + "|"
                if i == self.stackPointer:
                    out += "<-- pointer: " + str(self.stackPointer)
                out += "\n"

            out += "-" * (maxLen + 6) + "\n"

            print(out)
