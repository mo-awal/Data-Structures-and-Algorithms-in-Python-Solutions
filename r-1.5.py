"""
Give a single command that computes the sum from Ex. R-1.4,
relying on Python's comprehension syntax and the built-in sum
function
"""
n = int(input('Enter a positive integer: '))
sum(i*i for i in range(n))
