def single_number(arr):
    '''
    Input: a List of integers where every int except one shows up twice
    Returns: an integer

    >>> print(single_number([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))
    >>> 9
    '''
    # get first value in array
    current = arr[0]

    # loop through the rest of the array until find the same value
    for index, number in enumerate(arr[1:], 1):
        # if second value is found, swap it with the value at current index + 1 (1)
        if number == current:
            arr[1], arr[index] = arr[index], arr[1]
            # if found, repeat same process from current index + 2 after swap
            return single_number(arr[2:])
    
    # if the same value is not found return value
    return current    
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")