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
    # Friendly response
    friendly_response = "Alaris grins, her fingers flying across the keyboard as she types furiously. Okay, listen up! I'm going to walk you through this step-by-step."
    # Combine the friendly response with the bot response
    final_response = f"{friendly_response} {emoji.emojize(bot_response, use_aliases=True)}"
    await message.reply(final_response)
