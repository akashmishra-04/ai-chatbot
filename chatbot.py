from datetime import datetime
import random

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python developer go broke? Because he used up all his cache!",
    "Why was the computer cold? It forgot to close its windows!"
]

quotes = [
    "Success is the sum of small efforts repeated daily.",
    "Never stop learning.",
    "Practice makes progress.",
    "Dream big and work hard."
]

print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    # Save user message
    with open("chat_history.txt", "a") as file:
        file.write(f"You: {user}\n")

    if user == "hello":
        bot = "Hi! How can I help you today?"

    elif user == "how are you":
        bot = "I'm doing great! Thanks for asking."

    elif user == "what is your name":
        bot = "I am a Python AI Chatbot."

    elif user == "time":
        bot = datetime.now().strftime("Current Time: %H:%M:%S")

    elif user == "date":
        bot = datetime.now().strftime("Today's Date: %d-%m-%Y")

    elif user == "joke":
        bot = random.choice(jokes)

    elif user == "quote":
        bot = random.choice(quotes)

    elif user == "calculator":
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                bot = f"Answer: {num1 + num2}"
            elif op == "-":
                bot = f"Answer: {num1 - num2}"
            elif op == "*":
                bot = f"Answer: {num1 * num2}"
            elif op == "/":
                if num2 != 0:
                    bot = f"Answer: {num1 / num2}"
                else:
                    bot = "Cannot divide by zero."
            else:
                bot = "Invalid operator."

        except ValueError:
            bot = "Please enter valid numbers."

    elif user == "bye":
        bot = "Goodbye! Have a great day."
        print("Bot:", bot)

        with open("chat_history.txt", "a") as file:
            file.write(f"Bot: {bot}\n")

        break

    else:
        bot = "Sorry, I don't understand that command."

    print("Bot:", bot)

    # Save bot response
    with open("chat_history.txt", "a") as file:
        file.write(f"Bot: {bot}\n")