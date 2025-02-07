# imports
import requests
from Event import *
from IPython.display import Markdown, display

# Constants

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

system_prompt = """
You are an assistant working as an entity extractor. When one asks you to create an event for him, you extract entities as start datetime,
end datetime, summary, recurrence.
You answer only with a json built on the structure of a Google Calendar event. No explanation. No other words.
For example if prompt says:\n
dance lesson from 30 past ten pm to to 30 past eleven pm every Tuesday, Friday and Saturday\n
you respond:\n
{'summary': 'dance lesson', 'start': {'dateTime': "2025-02-07T22:30:00+02:00', 'timeZone':'Eastern European Time',"}, 'end': {'dateTime': "2025-06-30T23:30:00+02:00', 'timeZone':'Eastern European Time',"}, 'recurrence': ['RRULE:FREQ=WEEKLY;BYDAY=TU,FR,SA;UNTIL=20250630T000000Z']}
Start date of the event will be the first day after today.

"""

def getUserPrompt(user_prompt):
    prompt = "You are an assistant that creates Google Calendar events. Given this prompt:\n"
    prompt += user_prompt
    prompt += "\n you are supposed to return nothing else but a json formatted as a Google Calendar Event with the data given to the prompt."
    prompt += "\n If some crucial data is missing ask for it."
    return prompt

def getMessages(user_prompt):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": getUserPrompt(user_prompt)}
    ]

def askOllama(user_prompt):
    MODEL = "Llama3.2"
    # first approach using requests library
    payload = {
        "model": MODEL,
        "messages": getMessages(user_prompt),
        "stream": False
    }
    response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
    #print(response.json()['message']['content'])
    display(response.json()['message']['content'])

