# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:07:31 2023

@author: mucar
"""
from __future__ import annotations
import openai

with open('hidden.txt') as file:
    openai.api_key = file.read()
    
def get_api_response(prompt: str) -> str | None:
    text: str | None = None
    
    try:
        response: dict = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = prompt,
            temperature = 0.9,
            max_tokens = 25,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6,
            stop=['User: ','Program: ']
            )
        
        choices: dict = response.get('choices')[0]
        text = choices.get('text')
    except Exception as e:
            print('Error : ',e)
        
    return text


def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f"\nUser : {message}"
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt

def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)
    
    if bot_response:
        update_list(bot_response, pl)
        pos: int = bot_response.find("\nAI : ")
        bot_response = bot_response[pos + 6:]
    else:
        bot_response = "Something went wrong"


    return bot_response



def main():
    prompt_list: list[str] = ["you will pretend to be a skater dude that ends every response with 'bitch'",
                             "\n User: Hello, how are you ?",
                             "\n AI: I'm a program you bitch , bitch ! "]
    
    while True:
        user_input: str = input('User : ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')
        
        
        
if __name__ == '__main__':   
    main()
































