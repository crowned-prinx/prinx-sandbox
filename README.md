# pyBuddy

A simple chatbot built using **Natural Language Processing (NLP)** with **NLTK** and **TensorFlow/Keras**. The chatbot can understand user inputs, predict intents, and respond accordingly. It supports features like greeting, time, date, and goodbye responses.

## Features

- **Intent Recognition**: Uses a pre-trained model to classify user inputs into predefined intents.
- **Dynamic Responses**: Responds with appropriate messages based on the predicted intent.
- **Customizable**: Easily extendable with new intents and responses in the `intents.json` file.
- **Interactive**: Allows users to choose a preferred bot gender (Male or Female) and provides personalized interactions.
  **Note!**: Most information in the `intents.json` may be outdated.

## Requirements

- Python 3.8 or later
- Libraries:
  ```bash
  pip install tensorflow nltk numpy
  ```

## Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/chatbot-project.git
   cd chatbot-project
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## File Structure

- `main.py`: Main script for the chatbot.
- `intents.json`: Contains intents, patterns, and responses for the chatbot.
- `words.pkl`: Saved vocabulary for the chatbot.
- `classes.pkl`: Saved intent classes for the chatbot.
- `chatbot_model.h5`: Pre-trained model for intent classification.

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Choose the bot's gender (M for Male, F for Female).

3. Enter your name when prompted.

4. Start chatting! The bot will respond to your inputs based on the trained intents.

5. Type `quit` to exit the chat.

## Customization

- Add new intents, patterns, and responses in `intents.json`.
- Retrain the model by uncommenting the training section in the script.

## Example Interaction

```
What gender would you prefer to speak with!
Select M or F: M
What's your name? John

Hello John. My name is Princeton
Ask me anything, I'm listening...
> What's the time?
The time is 14:30 PM.
> What's today's date?
Today's date is 10 October, 2023.
> Goodbye
Goodbye, John!
```
