from app.chatbot import ChatBot

if __name__ == "__main__":
    bot = ChatBot("data/medical_faq_clean.csv")
    print("👩‍⚕️ MediBot: Hello! Ask me a medical question. Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👩‍⚕️ MediBot: Take care! 👋")
            break
        response = bot.get_response(user_input)
        print("👩‍⚕️ MediBot:", response)
