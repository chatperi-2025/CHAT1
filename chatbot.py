import nltk
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')


# Download necessary NLTK resources if they aren't already downloaded
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    print("Downloading required NLTK resources...")
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

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

# Main function to run the chatbot in a loop
def chatbot():
    print("ChatBot: Hello! I'm your NLP-powered chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower():
            print("ChatBot: Goodbye! Have a nice day.")
            break
        
        response = get_response(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
