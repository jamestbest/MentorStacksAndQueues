from Stacks.Stacks import VisualStack


class StackFrame:
    def __init__(self, returnAddress, localVariables, arguments):
        self.__returnAddress = returnAddress
        self.__localVariables = localVariables
        self.__arguments = arguments

    def __str__(self):
        return "Return Address: " + str(self.__returnAddress) \
            + " Local Variables: " + str(self.__localVariables) \
            + " Arguments: " + str(self.__arguments)

    def __len__(self):
        return len(self.__str__())


def PROGRAM_1():
    # STACK FRAME FOR PROGRAM 1

    stack = VisualStack(printVertical=True)

    print("PUSHING STACK FRAME FOR MAIN() FUNCTION AS SUB_A HAS BEEN CALLED")
    stack.push(StackFrame(3, {}, {}))

    print("PUSHING STACK FRAME FOR SUB_A FUNCTION AS SUB_B HAS BEEN CALLED")
    stack.push(StackFrame(6, {}, {"p1": 7}))

    print("PUSHING STACK FRAME FOR SUB_B FUNCTION AS SUB_C HAS BEEN CALLED")
    stack.push(StackFrame(12, {"x": 12, "z": "23"}, {"p10": 7, "y": 4}))

    print("PUSHING STACK FRAME FOR SUB_C FUNCTION AS PRINT HAS BEEN CALLED")
    stack.push(StackFrame(15, {}, {"p20": "23"}))

    print("POPPING STACK FRAME FOR SUB_C FUNCTION AS ENDSUB OF PRINT REACHED")
    stack.pop()

    print("POPPING STACK FRAME FOR SUB_B FUNCTION AS ENDSUB OF SUB_C REACHED")
    stack.pop()

    print("POPPING STACK FRAME FOR SUB_A FUNCTION AS ENDSUB OF SUB_B REACHED")
    stack.pop()

    print("PUSHING STACK FRAME FOR SUB_A FUNCTION AS SUB_C HAS BEEN CALLED")
    stack.push(StackFrame(7, {}, {"p1": 7}))

    print("PUSHING STACK FRAME FOR SUB_C FUNCTION AS PRINT HAS BEEN CALLED")
    stack.push(StackFrame(15, {}, {"p20": "8"}))

    print("POPPING STACK FRAME FOR SUB_C FUNCTION AS ENDSUB OF PRINT REACHED")
    stack.pop()

    print("POPPING STACK FRAME FOR SUB_A FUNCTION AS ENDSUB OF SUB_C REACHED")
    stack.pop()

    print("POPPING STACK FRAME FOR MAIN() FUNCTION AS ENDSUB OF SUB_A REACHED")
    stack.pop()

    print("STACK IS EMPTY: " + str(stack.is_Empty()))


def PROGRAM_2():
    # STACK FRAME FOR PROGRAM 2

    # RETURNS THE 5th FIBONACCI NUMBER

    stack = VisualStack(printVertical=True)

    print("PUSHING STACK FRAME FOR MAIN() FUNCTION AS FIB HAS BEEN CALLED")
    stack.push(StackFrame(2, {}, {}))

    print("PUSHING STACK FRAME FOR FIB(4) FUNCTION AS FIB(3) HAS BEEN CALLED")
    stack.push(StackFrame(10, {}, {"n": 4}))

    print("PUSHING STACK FRAME FOR FIB(3) FUNCTION AS FIB(2) HAS BEEN CALLED")
    stack.push(StackFrame(10, {}, {"n": 3}))

    print("PUSHING STACK FRAME FOR FIB(2) FUNCTION AS FIB(1) HAS BEEN CALLED")
    stack.push(StackFrame(10, {}, {"n": 2}))

    print("RETURN STATEMENT HAS BEEN REACHED AS 1 < 2 SO RETURNING n (1)")
    stack.pop()

    print("PUSHING STACK FRAME FOR FIB(2) FUNCTION AS FIB(0) HAS BEEN CALLED")
    stack.push(StackFrame(11, {"a": 1}, {"n": 2}))

    print("RETURN STATEMENT HAS BEEN REACHED AS 0 < 2 SO RETURNING n (0)")
    stack.pop()

    print("RETURN STATEMENT REACHED RETURNING a + b (1 + 0 = 1)")
    stack.pop()

    print("PUSHING STACK FRAME FOR FIB(3) FUNCTION AS FIB(1) HAS BEEN CALLED")
    stack.push(StackFrame(11, {"a": 1}, {"n": 3}))

    print("RETURN STATEMENT HAS BEEN REACHED AS 1 < 3 SO RETURNING n (1)")
    stack.pop()

    print("RETURN STATEMENT REACHED RETURNING a + b (1 + 1 = 2)")
    stack.pop()

    print("PUSHING STACK FRAME FOR FIB(4) FUNCTION AS FIB(2) HAS BEEN CALLED")
    stack.push(StackFrame(11, {"a": 2}, {"n": 4}))

    print("PUSHING STACK FRAME FOR FIB(2) FUNCTION AS FIB(1) HAS BEEN CALLED")
    stack.push(StackFrame(10, {}, {"n": 2}))

    print("RETURN STATEMENT HAS BEEN REACHED AS 1 < 2 SO RETURNING n (1)")
    stack.pop()

    print("PUSHING STACK FRAME FOR FIB(2) FUNCTION AS FIB(0) HAS BEEN CALLED")
    stack.push(StackFrame(11, {"a": 1}, {"n": 2}))

    print("RETURN STATEMENT HAS BEEN REACHED AS 0 < 2 SO RETURNING n (0)")
    stack.pop()

    print("RETURN STATEMENT REACHED RETURNING a + b (1 + 0 = 1)")
    stack.pop()

    print("RETURN STATEMENT REACHED RETURNING a + b (2 + 1 = 3)")
    stack.pop()

    print("PUSHING STACK FRAME FOR MAIN() FUNCTION AS PRINT HAS BEEN CALLED")
    stack.push(StackFrame(4, {"x": 3}, {}))

    print("POPPING STACK FRAME FOR MAIN() FUNCTION AS ENDSUB OF PRINT REACHED")
    stack.pop()

    print("REACHED END OF PROGRAM")


def main():
    # PROGRAM_1()
    # PROGRAM_2()
    print("end")
