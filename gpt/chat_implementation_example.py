import os
import openai
import keys

openai.organization = keys.oai_organization
openai.api_key = keys.oai_api_key
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

# Define conversation prompt(s)
prompt = ''

# Initialize converation state
state = {
    'prompt': prompt,
    'message': '',
}

def remove_first_section(text: str, max_length: int) -> str:
    # Check if text is already less than max_length
    if len(text) <= max_length:
        return text
    
    # Split text into sections
    sections = text.split('\n\n')

    # Remove first section until text is less than max_length
    while len('\n\n'.join(sections)) > max_length:
        sections = sections[1:]
    
    # Join remaining sections and return
    return '\n\n'.join(sections)


# Loop to contine conversation
while True:
    state['prompt'] = remove_first_section(state['prompt'], 300)

    user_input = input('User: ')
    state['prompt'] += user_input + '\n\n'

    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = state['prompt'],
        temperature = 0.5,
        max_tokens = 60,
        top_p = 1.0,
        frequency_penalty = 0.5,
        presence_penalty = 0.0,
        #stop = ['You!']
    )

    state['message'] = response.choices[0].text.strip() + '\n\n'
    state['prompt'] += state['message']

    # Print response to user
    print('JARVIS: ', state['message'])