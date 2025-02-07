import os
import requests
from dotenv import load_dotenv
from IPython.display import Markdown, display

import anthropic
# Load environment variables in a file called .env

load_dotenv()
api_key = os.getenv('ANTHROPIC_API_KEY')

# Check the key
if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-ant-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=api_key,
)

system_prompt = """
You are an assistant working as an entity extractor. When one asks you to create an event for him, you extract entities as start datetime,
end datetime, summary, recurrence.
You answer only with a json built on the structure of an iCalendar event. No explanation. No other words.
Start date of the event will be the first day after today.
"""


def getUserPrompt(user_prompt):
    prompt = "You are an assistant that creates iCalendar events. Given this prompt:\n"
    prompt += user_prompt
    prompt += "\n you are supposed to return nothing else but a json formatted as a Google Calendar Event with the data given to the prompt."
    prompt += "\n When one asks you to create an event for him, you extract entities as start datetime, end datetime, summary, recurrence."
    prompt += "\n If some crucial data is missing ask for it. Start date of the event will be the first day after today. It is important to remember: No explanation. No other word. Not suggestions."
    return prompt
    
    
def askClaude(user_prompt):
    return client.messages.create(
        #model="claude-3-5-sonnet-20241022", # fails. It returns text describing the event
        model = "claude-3-5-haiku-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": user_prompt}
        ])

# A function to display this nicely in the Jupyter output, using markdown

def displayClaudeResponse(user_prompt):
    response = askClaude(user_prompt)
    display(response.content[0])
