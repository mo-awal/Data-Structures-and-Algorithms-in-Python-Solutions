# R-1.6
def smallOddSquare(n):
    """Takes a positive integer n and returns the sum of the squares of all the
    odd positive integers smaller than n."""
    return sum(i*i for i in range(n) if i % 2)

if __name__ == '__main__':
    smallOddSquare(10)
    smallOddSquare(5)