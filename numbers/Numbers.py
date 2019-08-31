import itertools
import time

from UserInput import UserInput
from RpnCalculator import RpnCalculator


# 12, 1, 3, 4, 5, 6 ==> 33.
# python ==> 150s. pypy ==> 6s.

# 3, 3, 25, 50, 75, 100 ==> 996.
# python ==> cba to wait. pypy ==> 81s.

class Numbers:

    OPERATORS = ['+', '*', '-', '/']

    def __init__(self):
        self.user_input = UserInput()
        self.numbers = []
        self.target = 0
        self.rpn_calculator = None

    def run(self):
        self.user_input.get()
        print('\nComputing...')
        start_time = time.time()
        self.numbers = self.user_input.input_numbers
        self.target = self.user_input.input_target
        self.rpn_calculator = RpnCalculator(self.target)
        self._find_solution()
        end_time = time.time()
        print('Time elapsed: ' + str(round(end_time - start_time, 3)))

    def _find_solution(self):
        operator_permutations = itertools.combinations_with_replacement(self.OPERATORS, UserInput.NO_OF_NUMBERS-1)
        # 56 operator permutations if 6 numbers
        for op_perm in operator_permutations:
            numbers_and_ops = self.numbers + list(op_perm)
            print(numbers_and_ops)
            permutations = itertools.permutations(numbers_and_ops)  # 39916800 permutations if 6 numbers
            if self._compute_permutations(permutations):
                return
        print('No solution found')

    def _compute_permutations(self, permutations):
        for permutation in permutations:
            if self.rpn_calculator.calculate(permutation):
                print('\nSolution found!')
                print(self.rpn_calculator.correct_calculation)
                return True
        return False


Numbers().run()
