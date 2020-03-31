# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:37:56 2020

@author: Hanna Szczepanek
"""

import urllib.request
from bs4 import BeautifulSoup

print('Getting staff urls...')

staff_url = 'http://wa.amu.edu.pl/wa/en/staff_list'
response = urllib.request.urlopen(staff_url)
data = response.read()
doc = BeautifulSoup(data, 'html.parser')

print(doc)