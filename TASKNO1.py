import re

def rule_based_chatbot(user_input):
    # Define rules and responses
    rules = [
        {"pattern": r"hello|hi|hey", "response": "Hello! How can I help you?"},
        {"pattern": r"how are you", "response": "I'm just a program, but thanks for asking!"},
        {"pattern": r"bye|goodbye", "response": "Goodbye! If you need anything, feel free to ask."},
        {"pattern": r"your name", "response": "I'm your rule-based chatbot."},
        {"pattern": r"calculate (.+)", "response": lambda match: str(eval(match.group(1)))},
        {"pattern": r"date", "response": "The current date is: <insert current date here>"},
        {"pattern": r"time", "response": "The current time is: <insert current time here>"},
        {"pattern": r"weather (.+)", "response": "The weather in {} is <weather info>."},
        {"pattern": r"joke", "response": "Here's a joke: <insert joke here>"},
        {"pattern": r"reminder (.+)", "response": lambda match: f"I'll remind you of '{match.group(1)}' later."},
        {"pattern": r"search (.+)", "response": "Here are some search results for '{}': <insert results here>"},
        {"pattern": r"help", "response": "I can assist you with various tasks such as calculations, weather, jokes, and more."},
        {"pattern": r"define (.+)", "response": "The definition of '{}' is: <insert definition here>"},
        # Add more rules as needed
    ]

    # Check user input against rules
    for rule in rules:
        match = re.search(rule["pattern"], user_input, re.IGNORECASE)
        if match:
            if callable(rule["response"]):
                return rule["response"](match)
            else:
                return rule["response"]

    # Default response for unrecognized input
    return "I'm sorry, I don't understand that. Can you please rephrase or ask something else?"

# Example usage:
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = rule_based_chatbot(user_input)
    print("Chatbot:", response)