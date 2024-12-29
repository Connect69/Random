import os
from pyrogram import filters
import openai
from AnonXMusic import app 

# Set up your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"


# Define a function to generate a response using OpenAI's GPT-3 or GPT-4
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use "text-davinci-003" for GPT-3 or "gpt-4" if available
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.9,
    )
    return response.choices[0].text.strip()

# Handle incoming messages
@app.on_message(filters.text & ~filters.command)
def chat_with_user(client, message):
    user_input = message.text
    try:
        bot_response = generate_response(user_input)
        message.reply_text(bot_response)
    except Exception as e:
        message.reply_text("Oops! Something went wrong. Please try again later.")

