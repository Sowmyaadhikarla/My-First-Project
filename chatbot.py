print("🤖 Welcome to Chatbot! Have a great conversation 😊")
print("👉 If you want to exit, type 'Bye'.")

name = input("\n🧑 Your good name, please: ")

def greet(name):
    return f"\n👋 Hi {name}! 😊"

while True:
    response = input("You: ").lower()

    if response == "hi":
        print(greet(name))
    
    elif response == "what's your name?":
        print("🤖 I'm just a simple chatbot. You can call me Bot! 🤓")
        
    elif response == "how are you?":
        print("🤖 I'm just a bot, but I'm doing great! 😄\nAnd you?")

    elif response == "i'm fine":
        print("👍 Bot: Sounds good! 😃")
        
    elif response == "fine":
        print("👍 Bot: Sounds good! 😃")
        
    elif response == "not bad":
        print("🙂 Bot: Not bad is still good! Keep smiling! 😊")
    
    elif response == "i'm doing good":
        print("💪 Bot: Awesome! Keep it up! 🔥")
    
    elif response == "i'm also doing great":
        print("🙌 Bot: That's wonderful to hear! 🎉")
        
    elif response == "okay":
        print("👌 Okay, we’ll chat again! Take care 😊")
        
    elif response == "bye":
        print(f"👋 Goodbye, {name}! 🌟")
        print("✨ Have a nice day! ✨")
        break
    
    else:
        print("🤷‍♂️ Bot: Sorry, I can't understand what you're trying to say 😅")
