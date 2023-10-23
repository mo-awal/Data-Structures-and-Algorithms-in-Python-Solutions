"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd
"""
def existOddProduct(nums):
    """Takes a sequence of integer values and determines if there is a distinct
    pair of numbers in the sequence whose product is odd."""
    # if all the integers in num are even or only one odd integer, return False
    # if there is at least two odd numbers, return True
    num_odd_numbers = 0
    for x in nums:
        if num_odd_numbers >= 2:
            return True
        if x % 2:
            num_odd_numbers += 1
    return False
    
    
    ## Not efficient
    # if len([i for i in nums if i%2]) >= 2:
    #     return True
    # return False


print(existOddProduct([1, 2, 3, 4, 5]))
print(existOddProduct([1, 2, 4, 6]))
print(existOddProduct([2, 4, 6, 8, 10]))