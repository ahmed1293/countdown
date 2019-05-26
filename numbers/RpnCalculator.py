import operator

# https://en.wikipedia.org/wiki/Reverse_Polish_notation

OPERATORS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }


def rpn_calculate(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in OPERATORS:
            arg_2 = stack.pop()
            arg_1 = stack.pop()
            result = OPERATORS[token](arg_1, arg_2)
            stack.append(result)
        else:
            stack.append(int(token))

    final_result = stack.pop()
    return final_result

