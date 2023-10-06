# R-1.3

"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""
def minmax(data):
    """Return the smallest and largest numbers"""
    smallest = data[0]
    largest = data[0]
    for num in data:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return smallest, largest

if __name__ == '__main__':
    print(minmax([1,2,10,5,7,0]))
    print(minmax((1,)))
    print(minmax([0,9]))
    print(minmax(range(0, 12, 2)))
