import itertools
import time

from UserInput import UserInput
from RpnCalculator import RpnCalculator


# TODO: Use tqdm to print progress: https://github.com/tqdm/tqdm

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
            permutations = itertools.permutations(numbers_and_ops)  # 39916800 permutations if 6 numbers
            if self._compute_permutations(permutations):
                return
        print('No solution found')

    def _compute_permutations(self, permutations):
        solution_found = next(
            filter(lambda rpn: self.rpn_calculator.calculate(rpn), permutations),
            False
        )
        if solution_found:
            print('\nSolution found!')
            print(self.rpn_calculator.correct_calculation)
            return True
        return False


Numbers().run()
