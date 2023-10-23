# C-1.13
def reverse(nums):
    """Reverse a list of n integers"""
    i = 0
    j = len(nums)-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        j -= 1
        i += 1
    return nums


if __name__ == '__main__':
    print(reverse([2,3,4,5,6,7]))
    print(list(reversed([2,3,4,5,6,7])))
