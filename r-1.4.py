# R-1.4
def smallSquare(n):
    """Takes a positive integer n and returns the sum of the
    squares of all the positive integers smaller than n"""
    return sum(i*i for i in range(n))

if __name__ == '__main__':
    print(smallSquare((10)))
    print(smallSquare((1)))
