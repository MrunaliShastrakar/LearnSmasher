import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pairs = [
    [
        r"hello|hi|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"how are you|how's it going",
        ["I'm just a chatbot, but I'm here to assist you!", "I'm doing well. How can I assist you?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Have a great day!", "Bye! Feel free to come back anytime."]
    ],
    [
        r"(.*)",
        ["I'm sorry, but I'm just a simple chatbot and may not understand everything. Can you please rephrase?",]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Main loop to interact with the user
print("Chatbot: Hi there! I'm your chatbot. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
