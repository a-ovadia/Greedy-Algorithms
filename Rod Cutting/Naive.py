# Naive approach to rod cutting problem using dymanic programming


def maxRevenueNaive(length, sizes, prices):

    """
    Calculate the maximum revenue from cutting a rod using a naive recursive approach.

    This function uses dynamic programming to solve the rod cutting problem.
    It considers all possible ways to cut the rod and returns the maximum revenue.

    Args:
    length (int): The total length of the rod to be cut.
    sizes (list of int): A list of possible cut sizes.
    prices (list of float): A list of prices corresponding to each cut size.

    Returns:
    float: The maximum revenue that can be obtained from cutting the rod.

    Note:
    - This is a naive implementation with exponential time complexity.
    - For large inputs, this function may be slow due to redundant calculations.
    - The lengths of 'sizes' and 'prices' lists must be equal.

    Example:
    >>> L = 30
    >>> sizes = [1, 3, 5, 10, 30, 50, 75]
    >>> prices = [0.1, 0.2, 0.4, 0.9, 3.1, 5.1, 8.2]
    >>> maxRevenueNaive(L, sizes, prices)
    3.1
    """
        
    # Base Case 1: length is empty
    if length == 0:
        return 0
    
    # Base case 2: length is negative
    if length < 0:
        return float("-inf")
    
    # Store size of sizes
    len_sizes = len(sizes)
    # Initialize value lists
    valueRanges = []
    for value in range(len_sizes):
        valueRanges.append(prices[value] + maxRevenueNaive(length - sizes[value], sizes, prices))
    
    # Append zero to cover waste value
    valueRanges.append(0)

    # Return largest element from values list
    return max(valueRanges)

""" Example Usage"""
L = 30
sizes =  [ 1, 3, 5, 10, 30, 50, 75]
prices = [ 0.1, 0.2, 0.4, 0.9, 3.1, 5.1, 8.2]
print(maxRevenueNaive(L, sizes, prices))