"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""
def distinct(nums):
    """Takes a sequence of numbers and determines if all the numbers are distinct"""
    return len(set(nums)) == len(nums)
    