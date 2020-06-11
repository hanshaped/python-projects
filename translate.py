# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:43:18 2020

@author: Hanna Szczepanek
"""

from googletrans import Translator

def main():
    translator = Translator()
    result = translator.translate('How do you do?', dest='pl')
    print(result)
    
main()