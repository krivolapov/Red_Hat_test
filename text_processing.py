# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:23:15 2020

@author: Max
"""

import random

filename = "input.txt"

def paragraphs_shuffle(file_name):
    with open(file_name) as f:
        content = f.read()
        paragraphs = content.split("\n\n")
        print('\n\n'.join(random.sample(paragraphs, len(paragraphs))))


paragraphs_shuffle(filename)
