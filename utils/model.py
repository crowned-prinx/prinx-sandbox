import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

import random
import numpy as np
import random
import json
import pickle
import os


lemmatizer = WordNetLemmatizer()


with open('intents.json', 'r') as file:
    intents = json.load(file)

words = []
classes = []
documents = []
ignore_letters = ['!', '?', ',', '.']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print("documents:", documents)

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))
print("words:", words)

classes = sorted(set(classes))

# Save data  
# Check if files exist before saving
if not os.path.exists('words.pkl'):
    with open('includes/words.pkl', 'wb') as file:
        pickle.dump(words, file)
    print("words.pkl created and data saved.")
else:
    print("words.pkl already exists. Skipping save.")

if not os.path.exists('classes.pkl'):
    with open('includes/classes.pkl', 'wb') as file:
        pickle.dump(classes, file)
    print("classes.pkl created and data saved.")
else:
    print("classes.pkl already exists. Skipping save.")


training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])  # Append both bag and output_row as a single sublist

random.shuffle(training)
training = np.array(training, dtype=object)  # Use dtype=object to handle sublists of different lengths

train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

history = model.fit(np.array(train_x), np.array(train_y), epochs=100, batch_size=5, verbose=1 )
model.save('includes/chatbot_model.h5', history)

# print('Done!')