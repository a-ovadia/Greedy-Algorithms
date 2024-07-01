"""
Maximum Subarray Difference Algorithm

This module implements a divide-and-conquer algorithm to solve the maximum subarray difference problem.
The problem is to find the maximum difference between any two elements in an array,
where the larger element comes after the smaller element.

Usage:
    from max_subarray import maxSubarray

    # Example data
    data = [534, 35, 2, 5, 21, 5, 2]
    
    # Solve the maximum subarray difference problem
    result = maxSubarray(data, 0, len(data) - 1)
    print(f"The maximum subarray difference is: {result}")

Functions:
    maxSubarray(data, left, right): Main function to solve the problem
    minElement(data, left, right): Helper function to find minimum element in a range
    maxElement(data, left, right): Helper function to find maximum element in a range

Note:
    This algorithm has a time complexity of O(n log n) and a space complexity of O(log n)
    due to its recursive nature.

"""

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


# Example usage
if __name__ == "__main__":
    data = [534, 35, 2, 5, 21, 5, 2]
    result = maxSubarray(data, 0, len(data) - 1)
    print(f"The maximum subarray difference is: {result}")