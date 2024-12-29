import emoji
from transformers import pipeline
from pyrogram import filters
from pyrogram.types import Message
from AnonXMusic import app

# Load pre-trained conversational model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Define a function to process user input and generate a response
@app.on_message(filters.private & filters.text)
async def chat_with_bot(client, message: Message):
    user_input = message.text
    # Generate a response
    conversation = chatbot(user_input)
    bot_response = conversation[0]['generated_text']
    # Combine the friendly response with the bot response
    final_response = emoji.emojize(bot_response)
    await message.reply(final_response)