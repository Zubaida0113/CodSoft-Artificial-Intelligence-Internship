#author: Zubaida Sehnaz
import requests
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%I:%M:%S %p")  

def handle_query(query):
    # evaluate time
    if query == "what is time now":
        return "The current time is " + get_current_time()
    
    # Evaluate the arithmetic expression
    elif any(operator in query for operator in ['+', '-', '*', '/']):
        try:
            result = eval(query)  
            return f"The result is: {result}"
        except Exception as e:
            return "Sorry, I couldn't calculate that. Please enter a valid arithmetic expression."

    #evaluate defination    
    elif "define" in query:
        term = query.split("define ")[-1]
        return get_definition(term)
    else:
        return "I'm sorry, I didn't understand your query."

def get_definition(term):
    dictionary = {
        "ambivalent": "Having mixed feelings or contradictory ideas about something or someone.",
        "ecosystem": "A biological community of interacting organisms and their physical environment.",
        "democracy": "A system of government by the whole population or all the eligible members of a state, typically through elected representatives.",
        "computer":"A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations. Modern digital electronic computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks.",
        "marketing":"marketing is the process of creating, communicating, delivering, and exchanging offerings that have value for customers, clients, partners, and society at large.",
        "advertising":"Advertising is a marketing tactic that involves paying for space to promote a product, service, or cause to the public. The goal of advertising is to reach people who are likely to buy a company's products or services and entice them to do so."
    }
    
    if term in dictionary:
        return f"The definition of '{term}' is: {dictionary[term]}"
    else:
        return f"Sorry, I couldn't find a definition for '{term}'."

def simple_chatbot(user_input):
    rules = {
        "hi": "Hello! How can I help you?",
        "hello": "Hello! How can I help you?",
        "how are you": "I'm just a chatbot, but I'm doing well! How about you?",
        "how r u": "I'm just a chatbot, but I'm doing well! How about you?",
        "bye": "Goodbye! Have a great day!",
        "goodbye": "Goodbye! Have a great day!",
        "time": "what is time now",  
        "who is the prime minister of india":"Mr. Narendra Modi",
        "Who is the Prime Minister of India?":"Mr. Narendra Modi",
        "what is the capital of india?":"New Delhi"
    }

    user_input = user_input.lower()

    for rule, response in rules.items():
        if rule in user_input:
            if response == "what is time now":
                return handle_query(response)  
            return response

    return handle_query(user_input)

def main():
    print("Welcome to Simple_AI_ChatBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("SimpleChatBot: Goodbye! Have a great day!")
            break
        
        bot_response = simple_chatbot(user_input)
        print("SimpleChatBot:", bot_response)

if __name__ == "__main__":
    main()
