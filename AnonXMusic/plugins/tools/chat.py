import os
from pyrogram import filters
import openai
from AnonXMusic import app

# Set up your OpenAI API key
openai.api_key = "proj_Mh2EgJ6nfVc7tszL0gX7Za12"

# Define a function to generate a response using OpenAI's GPT-3 or GPT-4
async def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use "text-davinci-003" for GPT-3 or "gpt-4" if available
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Define a function to handle user input
async def handle_user_input(client, message):
    user_input = message.text
    try:
        bot_response = await generate_response(user_input)
        await message.reply_text(bot_response)
    except Exception as e:
        await message.reply_text("Oops! Something went wrong. Please try again later.")

# Handle incoming messages
@app.on_message(filters.private & filters.regex(r'^[^/].*'))
async def chat_with_user(client, message):
    await handle_user_input(client, message)