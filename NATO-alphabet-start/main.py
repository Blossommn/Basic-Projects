import pandas

letters = pandas.read_csv("nato_phonetic_alphabet.csv")

letters_dict = {row.letter: row.code for (index, row) in letters.iterrows()}


def generate_phonetic():
    word_input = input("Type in a word to translate: ").upper()
    try:
        phonetic_word = [letters_dict[letter] for letter in word_input]
    except KeyError as error_message:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_word)


generate_phonetic()
