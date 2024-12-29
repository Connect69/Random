import emoji
from transformers import pipeline
from pyrogram import filters
from pyrogram.types import Message
from AnonXMusic import app

# Load pre-trained chatbot model
chatbot = pipeline("chatbot", model="microsoft/DialoGPT-medium")

# Define a function to process user input and generate a response
@app.on_message(filters.private & filters.text)
async def chat_with_bot(client, message: Message):
    user_input = message.text
    # Generate a response based on the user input
    conversation = chatbot(user_input)
    bot_response = conversation[0]['generated_text']
    final_response = emoji.emojize(bot_response)
    await message.reply(final_response)