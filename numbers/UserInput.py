class UserInput:

    def __init__(self):
        self.input_numbers = None
        self.input_target = None

    def get(self):
        self._get_numbers_from_usr()
        self._get_target_from_usr()

    def _get_numbers_from_usr(self):
        while True:
            user_input = input("Enter 6 numbers separated by a space: ")

            input_list = user_input.split()

            if len(input_list) != 6:
                continue
            else:
                def convert_to_positive_int(string):
                    integer = int(string)
                    if integer <= 0:
                        raise ValueError
                try:
                    self.input_numbers = list(map(convert_to_positive_int, input_list))
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
