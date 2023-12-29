import pandas

# TODO 1. Create a dictionary in this format:
letters = pandas.read_csv("nato_phonetic_alphabet.csv")

# for (index, row) in letters.iterrows():
#     print(row.letter)

letters_dict = {row.letter: row.code for (index, row) in letters.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_input = input("Type in a word to translate: ").upper()

phonetic_word = [letters_dict[letter] for letter in word_input]
print(phonetic_word)