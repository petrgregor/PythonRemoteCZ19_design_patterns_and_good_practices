"""
Task 1 - Adapter

Using the Adapter pattern, write the wrapper to the list so that
the interface for the client will consist of the push, pop, and is_empty methods.

Create two implementations:

    based on an object adapter - use object composing
    based on a class adapter - use multi-inheritance to adapt the list interface to the expected stack interface

Use the created implementations to calculate the expressions given in the reverse Polish notation (RPN):

    '2 7 + 3 / 14 3 - 4 * + 2 /'
    '12 2 3 4 * 10 5 / + * +'
    '5 1 2 + 4 * + 3 -'
"""


class ClientInterface:
    def push(self, element):
        pass

    def pop(self):
        pass

    def is_empty(self):
        pass


# based on an object adapter - use object composing
class MyStack(ClientInterface):
    def __init__(self):
        self._data = []

    def push(self, element):
        self._data.append(element)

    def pop(self):
        return self._data.pop()

    def is_empty(self):
        return self._data.count == 0


def main():
    #expression = '2 7 + 3 / 14 3 - 4 * + 2 /'  # (((2 + 7) / 3) + ((14 - 3) * 4)) / 2 = 23.5
    #expression = '12 2 3 4 * 10 5 / + * +'     # 12 + (2 * ((3 * 4) + (10 / 5))) = 40
    expression = '5 1 2 + 4 * + 3 -'            # (5 + ((1 + 2) * 4)) - 3 = 14
    my_stack = MyStack()

    for element in expression.split():
        if element.isnumeric():
            my_stack.push(float(element))
        elif element == "+":
            my_stack.push(my_stack.pop() + my_stack.pop())
        elif element == "/":
            second_number = my_stack.pop()
            first_number = my_stack.pop()
            my_stack.push(first_number / second_number)
        elif element == "-":
            second_number = my_stack.pop()
            first_number = my_stack.pop()
            my_stack.push(first_number - second_number)
        elif element == "*":
            my_stack.push(my_stack.pop() * my_stack.pop())

    print(my_stack.pop())


if __name__ == "__main__":
    main()
