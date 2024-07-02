def bit_addition(val1 : int, val2 : int) -> list:
    """ 
    Function to compute bit addition
    Args:
        val1 (int): The first integer to add (in binary representation)
        val2 (int): The second integer to add (in binary representation)

    Returns:
        list: The addition result as a list of bits (most significant bit first)
    """

    max_length = max(val1.bit_length(), val2.bit_length())
    carry = 0
    # Initialze result bit string to the whichever val is larger + 1
    result = [0] * (max_length + 1)
    for num in range(max_length):
        bit1 = (val1 >> num) & 1
        bit2 = (val2 >> num) & 1
        (carry, result[num]) = sum_of_bits(bit1, bit2, carry)
    result[max_length] = carry

    # Return result in "reversed" to output correct format
    return result[::-1]

def sum_of_bits(num1 :int, num2 :int, carry :int) -> tuple[int, int]:
    """
    Helper function to sum two bits and a carry
    
    Args:
        num1 (int): First bit
        num2 (int): Second bit
        carry (int): Carry from previous addition

    Returns:
        tuple: (new_carry, result_bit)
    """
    result = None
    if carry == 0:
        if num1 == 1:
            if num2 == 0:
                result = 1
                carry = 0
            else:  # num2 = 1
                result = 0
                carry = 1
        elif num1 == 0:
            if num2 == 0:
                result = 0
                carry = 0
            else: # num2 == 1
                result = 1
                carry = 0
    elif carry == 1:
        if num1 == 1:
            if num2 == 1:
                result = 1
                carry = 1
            else:  # num2 == 0
                result = 0
                carry = 1
        elif num1 == 0:
            if num2 == 1:
                result = 0
                carry = 1
            else:  # num2 == 0
                result = 1
                carry = 0

    return (carry, result)