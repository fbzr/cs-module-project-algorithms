'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

Given an array of integers, there is a sliding window of size k which is moving from the left side of the array to the right, one element at a time. You can only interact with the k numbers in the window. Return an array consisting of the maximum value of each window of elements.
'''
def sliding_window_max(nums, k):
    # receive array of integers (nums) and a size of 'window' (k)

    # create a new list for the result
    result = []
    # while index (i) of element in array + size of window (k) is <= length of array (len(nums)):
    for i in range(len(nums) - k + 1):
        # create a variable to save the max value and initialize it with nums[i]
        max = nums[i]
        # loop through the rest of the window using its size (k)
        for idx in range(i+1, i+k):
            # value is higher than max value?
            if nums[idx] > max:
                # max value = new value
                max = nums[idx]
            
        # append max value to result array
        result.append(max)

    #return result array
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
