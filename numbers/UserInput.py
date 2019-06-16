class UserInput:

    NO_OF_NUMBERS = 6

    def __init__(self):
        self.input_numbers = None
        self.input_target = None

    def get(self):
        self._get_numbers_from_usr()
        self._get_target_from_usr()

    def _get_numbers_from_usr(self):
        while True:
            user_input = input(f'Enter {self.NO_OF_NUMBERS} numbers separated by a space: ')

            input_list = user_input.split()

            if len(input_list) != self.NO_OF_NUMBERS:
                continue
            else:
                def check_if_positive_int(string):
                    integer = int(string)
                    if integer <= 0:
                        raise ValueError
                    return integer
                try:
                    self.input_numbers = list(map(check_if_positive_int, input_list))
                except ValueError:
                    print("Positive integers only!")
                    continue
                return

    def _get_target_from_usr(self):
        while True:
            try:
                user_input = int(input("Enter the target number: "))
            except ValueError:
                print("Not an integer!")
                continue
            else:
                self.input_target = user_input
                return
