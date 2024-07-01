def maxSubarray(data, left, right):
    """ Function to solve the max subarray problem
        
        Args:
            data (list): The input array
            left (int): The left index of the subarray
            right (int): The right index of the subarray
    
        Returns:
            int: The maximum difference between any two elements where the larger comes after the smaller
    """
    
    # Base case 1 if 1 element
    if right == left:
        return 0
    # Base case
    elif right == left + 1:
        return max(data[right] - data[left], 0)
    
    # Find mid point
    mid = (left + right) // 2

    # Recursively call function on left subarray and right subarray
    leftSub = maxSubarray(data, left, mid)
    rightSub = maxSubarray(data, mid + 1, right)

    # Find minimum of left half and maximum of right half in the case the answer is found in both halves
    leftMin = minElement(data, left, mid )
    rightMax = maxElement(data, mid + 1, right)

    # Return the max
    return max(leftSub, rightSub, (rightMax - leftMin))

def minElement(data, left, right):
    """ Min helper function to find the smallest element in a array"""
    minEl = float("inf")
    for i in range(left, right + 1):
        minEl = min(minEl, data[i])
    return minEl

def maxElement(data, left, right):
    """ Max helper function to find the largest element in a array"""
    maxEl = float("-inf")
    for i in range(left, right + 1):
        maxEl = max(maxEl, data[i])
    return maxEl
