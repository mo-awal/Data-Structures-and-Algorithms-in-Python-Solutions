"""
A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos
"""

import random, string

sentence = "I will never spam my friends again"
num_typos = 0

def repeat_sentence():
    letters = string.ascii_letters
    for j in range(100):
        sentence_list = list(sentence)
        for i in random.sample(range(len(sentence)), 8):
            sentence_list[i] = random.choice(letters)
        print(f"{j+1:3}. {''.join(sentence_list)}.")


repeat_sentence()