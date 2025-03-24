r"""

@author: Prinx

Word Definition Lookup Program

This program allows users to look up the meaning of words from a JSON-based dictionary. 
It handles user input, suggests close matches for misspelled words, and displays definitions 
in a user-friendly format. The program uses the `difflib` library to provide suggestions 
for words not found in the dictionary and ensures robust error handling for file operations 
and JSON parsing.
"""



import json
from difflib import get_close_matches


def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON data: {e}")
        return None

def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input:
            return user_input
        print("Please enter a valid word.")

def define_word(word, data):
    if word == "END-PROGRAM":
        print("Thank you, goodbye! ;)")
        return

    if word in data:
        definitions = data[word]
        if isinstance(definitions, list):
            print(f"\nThere were {len(definitions)} definition(s) found for the word '{word.capitalize()}'.\n")
            for i, definition in enumerate(definitions, 1):
                print(f'{i}. {definition}')
        else:
            print(definitions)
    else:
        close_matches = get_close_matches(word, data.keys())
        if close_matches:
            print(f"\nSorry, couldn't find the word '{word.capitalize()}'.\nDo you mean {', '.join(close_matches)}?")
            response = get_user_input("If yes, type any of the correct word(s) above, else type N to end the program: ")
            if response != 'n':
                define_word(response, data)
            else:
                print("\nThank you, goodbye! ;)")
        else:
            print("Sorry, this word doesn't exist in our database, please try another word!")
