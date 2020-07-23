'''
Input: a List of integers
Returns: a List of integers

Sample input: [3, 0, 1, 0, -2]
Expected output: 3
Expected output array state: [3, 1, -2, 0, 0]

Sample input: [4, 2, 1, 5]
Expected output: 4
Expected output array state: [4, 2, 1, 5]
'''
def moving_zeroes(arr):
    # Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, then returns the altered array. The order of the non-zero integers does not matter in the mutated array.

    # loop through the list until find a non zero value
    # move that value to position 0

    # repeat the process till the end of list
    # return list

    # for i in range(len(arr)):
    #     if arr[i] != 0:
    #         value = arr.pop(i)
    #         arr.insert(0, value)
    
    # return arr

    ### Improved solution:
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            if arr[left] != 0:
                left += 1
            if arr[right] == 0:
                right -= 1


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")