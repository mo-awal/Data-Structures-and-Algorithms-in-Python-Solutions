"""
Write a Python program that inputs a list of words, 
separated by whitespace, and outputs how many times each
word appears in the list. You need not worry about efficiency at this point
"""

def count_words(words):
    counts = {}
    arr = words.split()
    for word in arr:
        counts[word] = counts.get(word, 0) + 1
    return counts


words = input('Enter words separated by whitespace:')
print(count_words(words))