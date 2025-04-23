from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data (ensures resources are available)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Initialize Flask app
app = Flask(__name__)

# Predefined responses
responses = {
    "greeting": ["hello", "hi", "hey", "greetings"],
    "goodbye": ["bye", "goodbye", "see you"],
    "name": ["your name", "who are you"],
    "feeling": ["how are you", "how do you do"],
    "help": ["help", "can you help", "i need help"]
}

# Function to get the response based on user input
def get_response(user_input):
    tokens = word_tokenize(user_input.lower())  # Tokenize user input

    for intent, keywords in responses.items():
        for word in tokens:
            if word in keywords:
                return generate_reply(intent)
    
    return "I'm not sure how to respond to that. Could you rephrase?"

# Function to generate a reply based on intent
def generate_reply(intent):
    replies = {
        "greeting": "Hi there! How can I assist you today?",
        "goodbye": "Goodbye! Talk to you later.",
        "name": "I'm an NLP chatbot created with Python and NLTK!",
        "feeling": "I'm just code, but I'm functioning as expected. 😄 How about you?",
        "help": "Sure! I can help answer questions or just chat."
    }
    return replies.get(intent, "I'm not sure how to respond to that. Could you rephrase?")

# Route for the web interface
@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_response = ""
    
    if request.method == "POST":
        user_input = request.form["message"]  # Get user input from form
        bot_response = get_response(user_input)  # Generate response
    
    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
