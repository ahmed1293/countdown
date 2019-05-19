class UserInput:

    def __init__(self, maximum_number_of_letters):
        self.input_letters = None
        self.minimum_word_length = 0
        self.maximum_number_of_letters = maximum_number_of_letters

    def get(self):
        self._get_letters_from_usr()
        self._get_minimum_word_length_from_usr()

    def _get_letters_from_usr(self):
        while True:
            user_input = input("Enter up to {} letters: ".format(self.maximum_number_of_letters))

            if len(user_input) > self.maximum_number_of_letters:
                print("That's more than {}!".format(self.maximum_number_of_letters))
                continue
            if not user_input.isalpha():
                print("Letters only!")
                continue

            self.input_letters = user_input.lower()
            return

    def _get_minimum_word_length_from_usr(self):
        while True:
            try:
                user_input = int(input("Enter the minimum word length: "))

                if user_input == 0:
                    print("Minimum cant be 0!")
                    continue
            except ValueError:
                print("Not an integer!")
                continue
            else:
                self.minimum_word_length = user_input
                return
