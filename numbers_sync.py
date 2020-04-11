import itertools
import sys
import time
from typing import Iterable, Optional
from user_input import get_numbers, get_target
from constants import OPERATORS, OPERATOR_FUNCS, NO_OF_NUMBERS


# 12 1 3 4 5 6 ==> 33.
# python ==> 150s. pypy ==> 6s.

# 3 3 25 50 75 100 ==> 996.
# python ==> cba to wait. pypy ==> 81s.


def check_if_solution(expression: Iterable, target: int) -> Optional[Iterable]:
    """Evaluates the RPN expression and returns it if the target is found"""
    stack = []
    for index, token in enumerate(expression):
        if token in OPERATORS:
            operator_func = OPERATOR_FUNCS[token]
            try:
                arg_2 = stack.pop()
                arg_1 = stack.pop()
                result = operator_func(arg_1, arg_2)
            except (IndexError, ZeroDivisionError):
                return
            stack.append(result)
            if result == target:  # check if intermediate calculation suffices
                return expression[0:index + 1]
        else:
            stack.append(token)
    final_result = stack.pop()
    if final_result == target:
        return expression


if __name__ == '__main__':
    _numbers = get_numbers()
    _target = get_target()
    start_time = time.time()

    # 56 operator permutations if 6 numbers
    operator_permutations = itertools.combinations_with_replacement(OPERATORS, NO_OF_NUMBERS-1)

    permutations = itertools.chain.from_iterable(
        # 39916800 permutations if 6 numbers
        [itertools.permutations(_numbers + list(op)) for op in operator_permutations]
    )

    for permutation in permutations:
        solution = check_if_solution(permutation, _target)
        if solution:
            print(f'\nSolution found: {solution}')
            print(f'Time elapsed: {str(round(time.time() - start_time, 3))}s')
            sys.exit()
    print('No solution found :(')
