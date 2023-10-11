# R-1.2
def is_even(k):
    """Return True if k is even"""
    return True if int(str(k)[-1]) in {0, 2, 4, 6, 8} else False

if __name__ == '__main__':
    print(is_even(12))
    print(is_even(9))
    print(is_even(1024))
    print(is_even(1025))
