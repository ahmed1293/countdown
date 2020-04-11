from user_input import get_letters, get_minimum_word_length


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
