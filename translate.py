# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:43:18 2020

@author: Hanna Szczepanek
"""

from googletrans import Translator

def main():
    translator = Translator()
    text = input('Type the word/phrase below:\n')
    result = translator.translate(text)
    print(result)
    
main()