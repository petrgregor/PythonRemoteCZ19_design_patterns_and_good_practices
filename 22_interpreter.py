class MathOperationApplier:
    def apply(self, math_operation, first, second):
        if math_operation == '+':
            return first + second
        elif math_operation == '-':
            return first - second
        elif math_operation == '*':
            return first * second
        elif math_operation == '/':
            return first / second
        elif math_operation == '**':
            return first ** second
        else:
            raise ArithmeticError()


class Interpreter:
    def interpret(self, context):
        pass


class PythonStyleWithoutOrderMathOperationsInterpreter(Interpreter):
    def __init__(self, math_operation_applier):
        self._math_operation_applier = math_operation_applier

    def interpret(self, context):
        split_data = context.strip().split()
        if len(split_data) % 2 == 0:
            raise ArithmeticError()

        value = float(split_data[0])
        for i in range(1, len(split_data), 2):
            value = self._math_operation_applier.apply(split_data[i], value, float(split_data[i+1]))
        return value


# TODO: zkusit implementovat interpreter i s prioritami výpočtu **, *, /, +, -

def main():
    math_operation_applier = MathOperationApplier()
    interpreter = PythonStyleWithoutOrderMathOperationsInterpreter(math_operation_applier)

    calculation = input('Choose a math operation: ')

    value = interpreter.interpret(calculation)

    print(value)


if __name__ == '__main__':
    main()
