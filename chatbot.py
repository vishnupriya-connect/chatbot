# chatbot.py
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_with_gpt(target, error, program):
    prompt = (f"Target: {target}\n"
              f"Error faced: {error}\n"
              f"Program in which error occurred: {program}\n"
              f"AI Task: Give correct code solving the error and explain what was the error and how it is solved in not more than 1 line.")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
