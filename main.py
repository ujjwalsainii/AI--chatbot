from transformers import pipeline


chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")

def completion(message):
    global chat_history

    
    chat_history += f"User: {message}\nBot:"

    # Generate reply
    response = chatbot(chat_history, max_new_tokens=200, pad_token_id=50256)[0]["generated_text"]

    # Extract only the bot’s part
    bot_reply = response.split("Bot:")[-1].strip()

    chat_history += f" {bot_reply}\n"
    print(f"Jarvis: {bot_reply}")

chat_history = ""

print("Jarvis: Hi! I am Jarvis, How may I help you?\n")
while True:
    user_question = input("User: ")
    completion(user_question)
