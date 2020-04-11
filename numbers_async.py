import asyncio
import itertools
import time
from concurrent import futures
from dataclasses import dataclass, field
from typing import Iterable, Optional

from constants import OPERATORS, OPERATOR_FUNCS
from user_input import get_numbers, get_target, NO_OF_NUMBERS


NO_OF_SOLUTIONS = 10


@dataclass
class ProcessesInfo:
    _solutions: set = field(default_factory=set)  # (identical solutions will exist)
    _process_count: int = 0
    _complete_calculations_count = 0

    @property
    def solutions(self):
        return self._solutions

    @property
    def complete_calculations_count(self):
        return self._complete_calculations_count

    @property
    def process_count(self):
        return self._process_count

    def add_solution(self, solution):
        self.solutions.add(solution)

    def increment_process_count(self):
        self._process_count += 1

    def increment_calculations_count(self):
        self._complete_calculations_count += 1


processes_info = ProcessesInfo()


def check_if_solution(expression: Iterable, target: int) -> Optional[Iterable]:
    """Evaluates the RPN expression and adds it to the solutions set it if the target is found"""
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
                processes_info.add_solution(expression[0:index + 1])
        else:
            stack.append(token)
    final_result = stack.pop()
    if final_result == target:
        processes_info.add_solution(expression)


def compute_permutations(permutations, target):
    for perm in permutations:
        if len(processes_info.solutions) > NO_OF_SOLUTIONS:
            break
        check_if_solution(perm, target)
        processes_info.increment_calculations_count()
    processes_info.increment_process_count()


def print_info(no_of_processes: int):
    while len(processes_info.solutions) < NO_OF_SOLUTIONS and processes_info.process_count < no_of_processes:
        solutions_info = f'Solutions found: {len(processes_info.solutions)} / {NO_OF_SOLUTIONS}'
        process_info = f'Complete processes: {processes_info.process_count} / {no_of_processes}'
        calc_info = f'Complete calculations: {processes_info.complete_calculations_count}'
        print(f'{solutions_info} --- {process_info} -- {calc_info}', end="\r", flush=True)
    print('\n')


async def main(numbers, target):
    # 56 operator permutations if 6 numbers
    operator_permutations = list(itertools.combinations_with_replacement(OPERATORS, NO_OF_NUMBERS-1))
    no_of_processes = len(operator_permutations)

    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, print_info, no_of_processes)

    # set of permutations for each combination of operators (list of lists)
    permutations = [itertools.permutations(numbers + list(op_perm)) for op_perm in operator_permutations]

    with futures.ThreadPoolExecutor(max_workers=no_of_processes) as executor:
        executor.map(lambda p: compute_permutations(p, target), permutations)

    while True:
        if len(processes_info.solutions) >= NO_OF_SOLUTIONS or processes_info.process_count == no_of_processes:
            return


if __name__ == '__main__':
    _numbers = get_numbers()
    _target = get_target()

    start_time = time.time()
    asyncio.run(main(numbers=_numbers, target=_target))

    # slice in case some process sneaks in an extra solution
    solutions_list = list(processes_info.solutions)[:NO_OF_SOLUTIONS]
    for s in solutions_list:
        print(s)
    print(f'Time elapsed: {str(round(time.time() - start_time, 3))}s')


# todo: seems to freeze after 24958658 calculations
#  reproduce: 3 3 25 50 75 100 with a high number of solutions
