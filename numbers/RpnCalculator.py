import operator

# https://en.wikipedia.org/wiki/Reverse_Polish_notation


class RpnCalculator:

    OPERATORS = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
    
    def __init__(self, target):
        self.target = target
        self.correct_calculation = None

    def calculate(self, expression):
        stack = []

        for index, token in enumerate(expression):
            if token in self.OPERATORS:
                try:
                    arg_2 = stack.pop()
                    arg_1 = stack.pop()
                    result = self.OPERATORS[token](arg_1, arg_2)
                except (IndexError, ZeroDivisionError):
                    return False
                stack.append(result)
                if result == self.target:  # check if intermediate calculation suffices
                    self.correct_calculation = expression[0:index+1]
                    return True
            else:
                stack.append(int(token))

        final_result = stack.pop()
        if final_result == self.target:
            self.correct_calculation = expression
            return True
        return False

