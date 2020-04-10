MAX_NO_OF_LETTERS = 30


def get_letters():
    while True:
        user_input = input(f'Enter up to {MAX_NO_OF_LETTERS} letters: ')
        if len(user_input) > MAX_NO_OF_LETTERS:
            print(f"That's more than {MAX_NO_OF_LETTERS}!")
            continue
        if not user_input.isalpha():
            print('Letters only!')
            continue
        return ''.join(sorted(user_input.lower()))


def get_minimum_word_length():
    while True:
        try:
            user_input = int(input('Enter the minimum word length: '))
            if user_input == 0:
                print("Minimum cant be 0!")
                continue
        except ValueError:
            print("Not an integer!")
            continue
        return user_input


if __name__ == '__main__':
    letters = get_letters()
    min_length = get_minimum_word_length()

    words = []

    with open('/usr/share/dict/words') as words_file:
        for word in words_file.readlines():
            letters_in_word = ''.join(sorted(word.strip()))
            if len(letters_in_word) > min_length and letters_in_word in letters:
                words.append(word)

    print(''.join(words))
