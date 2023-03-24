import openai
import keys
from model_descriptions import *

openai.organization = keys.oai_organization
openai.api_key = keys.oai_api_key

cost = 0.000000
character_limit = 10000
full_context = ''

# Prices are per 1k tokens. Whisper is per second.
all_models = {
    'gpt-4': {'version': 'gpt4', 'snapshot': 'gpt-4-0314', 'price_prompt': 0.03, 'price_completion': 0.06, 'long_des': gpt4_long, 'short_des': gpt4_short, 'good_at': gpt4_good}, 
    'gpt-4-32k': {'version': 'gpt4', 'snapshot': 'gpt-4-32k-0314', 'price_prompt': 0.06, 'price_completion': 0.12, 'long_des': gpt4_32k_long, 'short_des': gpt4_32k_short, 'good_at': gpt4_32k_good}, 
    'gpt-3.5-turbo': {'version': 'gpt3.5', 'snapshot': 'gpt-3.5-turbo-0301', 'price': 0.002, 'long_des': gpt35_turbo_long, 'short_des': gpt35_turbo_short, 'good_at': gpt35_turbo_good},
    'text-davinci-003': {'version': 'gpt3.5', 'price': 0.02, 'long_des': davinci_long, 'short_des': davinci_short, 'good_at': davinci_good}, 
    'text-curie-001': {'version': 'gpt3', 'price': 0.002, 'long_des': curie_long, 'short_des': curie_short, 'good_at': curie_good},
    'text-babbage-001': {'version': 'gpt3', 'price': 0.005, 'long_des': babbage_long, 'short_des': babbage_short, 'good_at': babbage_good},
    'text-ada-001': {'version': 'gpt3', 'price': 0.0004, 'long_des': ada_long, 'short_des': ada_short, 'good_at': ada_good},
    'whisper': {'price': 0.0001, 'long_des': whisper_long}, 
    'codex': {'code-davinci-002': 0, 'code-cushman-001' : 0, 'long_des': codex_long, 'davinci_des': codex_davinci_short, 'cushman_des': codex_cushman_short, 'good_at': codex_good}, 
    }


def add_cost(the_response):
    global cost

    if the_response.model in ['gpt-3.5-turbo', 'gpt-3.5-turbo-0301', 'text-davinci-003', 'text-curie-001', 'text-babbage-001', 'text-ada-001']:
        cost += ((the_response.usage.total_tokens / 1000) * all_models[the_response.model]['price'])
    elif the_response.model in ['code-davinci-002', 'code-cushman-001']:
        cost = 0.000000


def remove_first_section(text: str, max_char_length: int) -> str:
    # Check if text is already less than max_length
    if len(text) <= max_char_length:
        return text
    
    # Split text into sections
    sections = text.split('\n\n')

    # Remove first section until text is less than max_length
    while len('\n\n'.join(sections)) > max_char_length:
        sections = sections[1:]
    
    # Join remaining sections and return
    return '\n\n'.join(sections)


def chat_model():
    global full_context
    global character_limit

    user_input = ''
    response_text = ''

    while user_input != "thanks, done":
        user_input = input('User: ')

        full_context += f'Prompt: {user_input} '

        full_context = remove_first_section(full_context, character_limit)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "You are a helpful assistant named Jarvis. You are occassionally witty, funny, and sarcastic, but always helpful. You answer conciesly using only one sentence unless asked to elaborate."},
            {"role": "user", "content": full_context}
            ],
        )

        add_cost(response)

        response_text = response.choices[0].message.content.strip()
        full_context += f'JARVIS: {response_text} '

        print(f'{response_text}')

    print('\n---------------stats---------------')
    print(f'The model used was {response.model}')
    print(f'The total cost of this conversation was ${cost}')
    print('-----------------------------------')


def instruct_model():
    user_input = ''

    while user_input != "thanks, done":
        user_input = input('User: ')

        response = openai.Completion.create(
            engine = 'text-ada-001',
            prompt = user_input,
            temperature = 0.5,
            max_tokens = 100,
            top_p = 1.0,
            frequency_penalty = 0.5,
            presence_penalty = 0.0,
            #stop = ['You!']
        )

        add_cost(response)

        print(f'InstructGPT ({response.model[5:8]}): {response.choices[0].text.strip()}')

        

    print('\n---------------stats---------------')
    print(f'The model used was {response.model}')
    print(f'The total cost of this conversation was ${cost:.8f}')
    print('-----------------------------------')


if __name__ == "__main__":
    chat_model()