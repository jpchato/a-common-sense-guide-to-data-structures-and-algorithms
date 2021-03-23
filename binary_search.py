def binary_search(arr, val):
    # first , we establish the lower and upper bounds of where the value we're searching for can be. To start, the lower boudn is the first value in the array, while the upper bound is the last value
    
    lower_bound_index = 0
    upper_bound_index = len(arr) - 1
    # we begin a loop in which we keep inspecting the middlemost value between the upper and lower bounds:
    while lower_bound_index <= upper_bound_index:
        # find the middlepoitn between the upper and lower bounds: 
        midpoint_index = (upper_bound_index + lower_bound_index)//2
        
        # we inspect the value at the midpoint
        value_at_midpoint = arr[midpoint_index]
        # If the value at the midpoint is the one we're looking for, we're done. If not, we change the lower or upper bound based on whether we need to guess higher or lwoer:
        if val < value_at_midpoint:
            upper_bound_index = midpoint_index - 1
        elif val > value_at_midpoint:
           lower_bound_index = midpoint_index + 1
        elif val == value_at_midpoint:
            print(f'midpoint index: {midpoint_index}, midpoint value: {value_at_midpoint}')
            return midpoint_index
    #  If we've narrowed the bounds until they've reached each other, that means that the value we're searching for is not in the array
    return None 

# binary_search([1,2,3,4,5,6,7,8,9], 5)
if __name__ == '__main__':
    binary_search([1,2,3,4,5,6,7,8,9], 5)