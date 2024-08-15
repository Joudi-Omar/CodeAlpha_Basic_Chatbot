import random

# Define patterns and responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "name": ["I am a chatbot created to assist you.", "You can call me Chatbot!"],
    "how are you": ["I'm just a bunch of code, but I'm here to help you!", "I'm doing well, thanks for asking!"],
    "from where are you": ["I exist in the digital world, so you could say I'm from everywhere and nowhere!"],
    "what can you do": ["I can chat with you, answer your questions, and help with simple tasks."],
    "What's the weather like?":["I'm not connected to the internet, so I can't check the weather for you, but you can try a weather app!"],
    "How old are you?":["I don't have an age, but I was created recently!"],
    "Where are you from?":["I live in the cloud!"],
    "What are your hobbies?":["I love chatting with people! It's my main hobby."],
    "What is your favorite color?":["I don't have eyes, but I hear blue is a nice color"],
    "What is your favorite food?":["I don't eat, but I think digital cookies sound good!"],
    "Do you have any friends?":["I have lots of friends who chat with me just like you!"],
    "Thank you":["Do you have any more questions?"],
    "exit": ["Goodbye! It was nice talking to you.", "See you later!", "Goodbye!"]
}

# Default response if no match is found
default_response = "I'm not sure I understand. Can you rephrase that?"
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return default_response
def chatbot():
    print("Hi! I am your chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("> ")
        if "exit" in user_input.lower():
            print(random.choice(responses["exit"]))
            break
        print(get_response(user_input))

if __name__ == "__main__":
    chatbot()
