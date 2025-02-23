
r"""

@author: Prinx

Word Definition Lookup Program

This program allows users to look up the meaning of words from a JSON-based dictionary. 
It handles user input, suggests close matches for misspelled words, and displays definitions 
in a user-friendly format. The program uses the `difflib` library to provide suggestions 
for words not found in the dictionary and ensures robust error handling for file operations 
and JSON parsing.
"""

from utils.functions import load_data, get_user_input, define_word

# Path to JSON-based dictionary file
dict_path = "./data/data.json"

def main():
    data = load_data(dict_path)
    if data:
        word = get_user_input("Enter a word to find its meaning: ")
        define_word(word, data)

if __name__ == "__main__":
    main()