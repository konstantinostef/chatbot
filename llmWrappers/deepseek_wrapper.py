# imports

import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI

# Load environment variables in a file called .env

load_dotenv()
api_key = os.getenv('DEEPSEEK_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")

openai = OpenAI()

# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."
today = datetime.today().strftime("%Y-%m-%d")

system_prompt = """
You are an assistant working as an entity extractor. When one asks you to create an event for him, you extract entities as start datetime,
end datetime, summary, recurrence.
You answer only with a json built on the structure of an iCalendar event. No explanation. No other words.
Start date of the event will be the first day after today.
"""
system_prompt += f"Today is {today}."


def getUserPrompt(user_prompt):
    prompt = "You are an assistant that creates iCalendar events. Given this prompt:\n"
    prompt += user_prompt
    prompt += "\n you are supposed to return nothing else but a json formatted as a Google Calendar Event with the data given to the prompt."
    prompt += "\n If some crucial data is missing ask for it."
    return prompt
    

def getMessages(user_prompt):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": getUserPrompt(user_prompt)}
    ]

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")


def askDeepSeek(user_prompt):
    response = client.chat.completions.create(
        model = "deepseek-chat",
        messages = getMessages(user_prompt),
        stream=False
    )
    return response

# A function to display this nicely in the Jupyter output, using markdown

def displayDeepSeekResponse(user_prompt):
    response = askDeepSeek(user_prompt)
    display(response)
