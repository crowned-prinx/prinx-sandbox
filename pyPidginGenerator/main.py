from flask import Flask, jsonify, request, render_template
import os
import google.generativeai as genai
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Your API key should be stored in a .env file
# You can obtain an API key by signing up at https://console.generativeai.com
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# SYS_INSTRUCT is an environment variable that contains the system instruction
# This is used to set the system instruction for the model
model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction=os.getenv("SYS_INSTRUCT"),
)

chat_session = model.start_chat(
  history=[
  ]
)

# Route to get the API version and usage instructions
@app.route('/', methods=['GET'])
def get_items():
    return render_template('index.html')


@app.route('/translate', methods=['POST'])
def translate_to_pidgin():
    """
    Translates English text to Pidgin using the Gemini model.
    Expects a JSON payload with a "text" and an optional "tone" field.
    Returns a JSON response with the translated text.
    """
    try:
        data = request.get_json()
        if "text" not in data:
            return jsonify({"error": "Missing 'text' field in request"}), 400

        english_text = data["text"].strip()
        if not english_text:  # Check if text is empty after stripping whitespace
            return jsonify({"error": "Text to translate cannot be empty"}), 400

        if "tone" not in data:
            tone = "an informal"
        else:
            tone = data["tone"].strip().lower()
            if tone in ["informal", "formal"]:
                if tone == "informal":
                    tone = "an informal"
                else:
                    tone = "a formal"
            else:
                return jsonify({"error": "Invalid tone. Must be 'informal' or 'formal'"}), 400

        
        prompt = (
                    f'You are a language translator. Your task is to convert the following text to {tone} Pidgin if it is in English, '
                    f'or to grammatically correct English if it is in Pidgin. '
                    f'For example: '
                    f'1. Input: "How are you?" → Output: "How you dey?" '
                    f'2. Input: "How you dey?" → Output: "How are you?" '
                    f'Here is the text: "{english_text}". '
                    f'Return only the converted text without any additional explanations or formatting.'
                )

        response = chat_session.send_message(prompt)
        pidgin_text = response.text

        return jsonify({"pidgin_text": pidgin_text})

    except Exception as e:
        print(f"Error during translation: {e}")
        return jsonify({"error": "Translation failed"}), 500


if __name__ == '__main__':
    app.run(debug=False)