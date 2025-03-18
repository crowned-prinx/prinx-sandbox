import nltk
import datetime
import random
import numpy as np
import pickle
import json
from tensorflow.keras.models import load_model
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

class Chat:
    def __init__(self, intents_file='includes/intents.json', words_file='includes/words.pkl', classes_file='includes/classes.pkl', model_file='includes/chatbot_model.h5'):
        # Initialize the lemmatizer
        self.lemmatizer = WordNetLemmatizer()

        # Load intents, words, classes, and model
        with open(intents_file, 'r') as file:
            self.intents = json.load(file)
        with open(words_file, 'rb') as file:
            self.words = pickle.load(file)
        with open(classes_file, 'rb') as file:
            self.classes = pickle.load(file)
        self.model = load_model(model_file)

    def clean_up_sentence(self, sentence):
        """Tokenize and lemmatize a sentence."""
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words

    def bag_of_words(self, sentence):
        """Convert a sentence into a bag of words."""
        sentence_word = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for w in sentence_word:
            for i, word in enumerate(self.words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)

    def predict_class(self, sentence):
        """Predict the intent of a sentence."""
        bow = self.bag_of_words(sentence)
        res = self.model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({'intent': self.classes[r[0]], 'probability': str(r[1])})
        return return_list

    def get_response(self, intents_list):
        """Get a response based on the predicted intent."""
        tag = intents_list[0]['intent']
        list_of_intents = self.intents['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
        return result

    def speak(self, bot_name, user_name):
        """Start a conversation with the chatbot."""
        print(f"\n{self.shuff_greeting()} {user_name.capitalize()}. My name is {bot_name}\n")
        print("Ask me anything, I'm listening...")
        while True:
            message = input("").lower()
            if message == "quit":
                break
            ints = self.predict_class(message)
            if not ints or float(ints[0]['probability']) < 0.7:
                print(f"Sorry {user_name}, I didn't get that, please can you re-phrase")
                continue
            else:
                tag = ints[0]['intent']
                res = self.get_response(ints)
                if tag == "name":
                    print(f"{res} {bot_name}")
                elif tag == "date":
                    current_date = datetime.datetime.now().strftime("%d %B, %Y")
                    print(f"{res} Today's date is {current_date}")
                elif tag == "time":
                    current_time = datetime.datetime.now().strftime("%H:%M: %p")
                    print(f"{res} The time is {current_time}")
                elif tag == "gender":
                    gender_response = "Female" if bot_name == "Princess" else "Male"
                    print(f"{res} {gender_response}")
                elif tag == "goodbye":
                    print(f"{res} {user_name.capitalize()}")
                else:
                    print(res)

    def shuff_greeting(self):
        """Return a random greeting."""
        shuff = ["hello", "hi", "hy", "hey"]
        return random.choice(shuff).capitalize()

    def filter_name(self, name_list, gender):
        """Filter and format the user's name."""
        name_list = list(name_list.split())
        words = ["i", "i'm", "im", "am", "my", "is", "name", "names", "you", "can", "call", "me", "just", "yeah", "and", "are", "hey", "okay", "alright"]
        filtered_name = [name.capitalize() for name in name_list if name not in words]
        return ' '.join(filtered_name)

    def ask_name(self, gender):
        """Ask for the user's name and filter it."""
        name = input("What's your name? ")
        if not name:
            print("Please enter a name.")
            self.ask_name(gender)
        else:
            user_name = self.filter_name(name, gender)
            bot_name = "Princeton" if gender == "M" else "Princess"
            self.speak(bot_name, user_name)