import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from pyrogram import filters
from pyrogram.types import Message
from AnonXMusic import app

# Load pre-trained model and tokenizer
model_name = "t5-base"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

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