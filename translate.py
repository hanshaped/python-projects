# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:43:18 2020

@author: Hanna Szczepanek
"""

from googletrans import Translator
import requests

def googletrans():
    translator = Translator()
    text = input('Type the word/phrase below:\n')
    result = translator.translate(text)
    print(result)
    
def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
    
    response = requests.post(url, data=data)
    print(response.text)
    
piratetrans('Hello, sir')