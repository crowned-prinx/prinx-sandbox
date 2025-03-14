# Speech Recognition Word Guessing Game

A simple Python game where you guess a word by speaking it aloud. The game uses speech recognition to transcribe your guess and checks if it matches the randomly selected word.

## How It Works

1. The game selects a random word from a predefined list.
2. You have a limited number of attempts to guess the word by speaking into your microphone.
3. The game uses the `speech_recognition` library to transcribe your speech and checks if it matches the target word.
4. If you guess correctly, you win! Otherwise, you lose after exhausting all attempts.

## Requirements

- Python 3.x
- `speechrecognition` library (`pip install SpeechRecognition`)
- A working microphone

## How to Run

1. Install the required library:
   ```bash
   pip install SpeechRecognition
   ```
2. Download or clone the repository.
3. Run the game:
   ```bash
   python game.py
   ```
4. Follow the on-screen instructions and speak your guesses into the microphone.

## Features

- Real-time speech recognition using Google's Speech-to-Text API.
- A list of words to guess from.
- Limited attempts to make the game challenging.
- Clear feedback on whether your guess was correct or not.

## Example

```
I'm thinking of one of these words:
apple, banana, peach, orange, lemon, lime, kiwi, cherry, fig
You have 3 tries to guess which one.

Guess 1. Speak now!
You said: banana
Incorrect. Try again.

Guess 2. Speak now!
You said: apple
Correct! You win!
```

## Notes

- Ensure your microphone is working properly.
- Speak clearly for better transcription accuracy.
- If the API is unavailable, the game will notify you and exit.
