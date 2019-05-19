import time

from UserInput import UserInput


class LettersToWords:

    def __init__(self):
        self.user_input = UserInput(maximum_number_of_letters=30)
        self.words_file = None
        self.matching_words = []

    def run(self):
        self.user_input.get()
        start_time = time.time()
        self.words_file = open('/usr/share/dict/words')
        self._find_matches()
        self.words_file.close()
        self._print_list()
        end_time = time.time()
        print("Time elapsed: " + str(round(end_time - start_time, 3)))

    def _find_matches(self):
        minimum_word_length = self.user_input.minimum_word_length

        for word in self.words_file.readlines():
            word = word[:-1]
            if len(word) >= minimum_word_length and self._all_letters_match(word.lower()):
                self.matching_words.append(word)
        self.matching_words.sort(key=len)

    def _all_letters_match(self, word):
        input_letters = self.user_input.input_letters
        for letter in word:
            if letter in input_letters:
                input_letters = input_letters.replace(letter, "", 1)
            else:
                return False
        return True

    def _print_list(self):
        for word in self.matching_words:
            print(word)


LettersToWords().run()

