def repeat_divide(n):
    """Takes a positive integer n > 2 as input and returns the
    number of times one must repeatedly divide n by 2 before getting
    a value less than 2"""
    count = 0
    while n >= 2:
        n = n / 2
        count += 1
    return count

def repeat_divide_rec(n):
    """A recursive solution"""
    if n < 2:
        return 0
    else:
        return 1 + repeat_divide_rec(n/2)


print(repeat_divide(10))
print(repeat_divide(5))
print(repeat_divide(3))
print(repeat_divide(32))

print()
print(repeat_divide_rec(10))
print(repeat_divide_rec(5))
print(repeat_divide_rec(3))
print(repeat_divide_rec(32))
