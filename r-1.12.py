import random

"""
Python's random module includes a function choice(data) that 
returns arandom element from a non-empty sequence. The random
module includes a more basic function randrange, with 
parameterization similar to the built-in range function, that
return a random choice from the given range. Using only the 
randrange function, implement your own version
of the choice function.
"""

def choice(seq):
    """Our own implementation of random.choice"""
    index = random.randrange(len(seq))
    return seq[index]


print(choice([1, 2, 3, 4, 5]))
