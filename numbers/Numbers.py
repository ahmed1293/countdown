import itertools
import time

from UserInput import UserInput
from RpnCalculator import RpnCalculator


# Figure out how to speed this up...
# Use 4 numbers for now (to make testing quicker)?
# Try get to 30 secs maximum, with 6 numbers

class Numbers:

    OPERATORS = ['+', '-', '*', '/']

    def __init__(self):
        self.user_input = UserInput()
        self.numbers = []
        self.target = 0

    def run(self):
        self.user_input.get()
        start_time = time.time()
        self.numbers = self.user_input.input_numbers
        self.target = self.user_input.input_target
        self._compute_all_combinations()
        end_time = time.time()
        print("Time elapsed: " + str(round(end_time - start_time, 3)))

    def _compute_all_combinations(self):
        rpn_calculator = RpnCalculator(self.target)
        operator_permutations = itertools.combinations_with_replacement(self.OPERATORS, 5)
        attempt = 0
        for op_perm in operator_permutations:
            numbers_and_ops = self.numbers + list(op_perm)
            permutations = itertools.permutations(numbers_and_ops)
            valid_rpn = [rpn for rpn in permutations if rpn_calculator.is_valid(rpn)]
            for permutation in valid_rpn:
                attempt += 1
                if rpn_calculator.calculate(permutation):
                    print(rpn_calculator.correct_calculation)
                    print(f'Attempts made: {attempt}')
                    return
                else:
                    print(f'Attempt {attempt}', end='\r')
        print('No solution found')


Numbers().run()
