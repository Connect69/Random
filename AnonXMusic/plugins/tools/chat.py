import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from pyrogram import filters
from pyrogram.types import Message
from AnonXMusic import app

# Load pre-trained model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-base")
tokenizer = T5Tokenizer.from_pretrained("t5-base")

# Define a function to process user input and generate a response
@app.on_message(filters.private & filters.text)
async def chat_with_bot(client, message: Message):
    user_input = message.text
    # Tokenize user input
    inputs = tokenizer(user_input, return_tensors="pt")
    # Generate response
    outputs = model.generate(inputs["input_ids"], max_length=100)
    # Convert response to text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    await message.reply(response)