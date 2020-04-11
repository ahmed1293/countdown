from typing import List
from constants import MAX_NO_OF_LETTERS, NO_OF_NUMBERS


def get_letters() -> str:
    while True:
        user_input = input(f'Enter up to {MAX_NO_OF_LETTERS} letters: ')
        if len(user_input) > MAX_NO_OF_LETTERS:
            print(f"That's more than {MAX_NO_OF_LETTERS}!")
            continue
        if not user_input.isalpha():
            print('Letters only!')
            continue
        return ''.join(sorted(user_input.lower()))


def get_minimum_word_length() -> int:
    while True:
        user_input = input('Enter the minimum word length: ')
        if user_input == 0:
            print("Minimum cant be 0!")
            continue
        if not user_input.isdigit():
            print("Not an integer!")
            continue
        return int(user_input)


def get_numbers() -> List[int]:
    while True:
        user_input = input(f'Enter {NO_OF_NUMBERS} numbers separated by a space: ')
        input_list = user_input.split()

        if len(input_list) != NO_OF_NUMBERS:
            continue

        errors = [n for n in input_list if not n.isdigit() or int(n) <= 0]
        if errors:
            continue
        return list(map(int, input_list))


def get_target() -> int:
    while True:
        user_input = input("Enter the target number: ")
        if not user_input.isdigit() or int(user_input) <= 0:
            continue
        return int(user_input)
