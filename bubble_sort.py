# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:46:47 2020
@author: Drew

This is a bubble sort. It works by going through pairs
of elements in the list in order and swapping them if 
the 1st element is greater than the 2nd (if i>i+1). 
It is called bubble sort as the larger numbers go to
end like like bubbles rising, while smaller ones sink.


The compexity of this algorithm is O(n^2).
The worst case is if the list is backwards.
If so, we need to swap every element. 
The algorithm works by going through each element,
and if the flag is true, runs the algo. As such,
there are 2 n's to go through, so n^2.

This is inefficient as it repeats (for loops) for each 
element in the list. Thus, even if just the first 2 elements
needed to be swapped, it will run for every element regardless.

"""

# This is an implementation of the bubble sort algorithm.
# The algorithm accepts a numbered list (ordered or unordered)
# It makes modifications to the original list, and returns 0
def bubble(num_list):
    # Start with a True start condition so we can get into the loop.
    in_order = True
    # A while loop allows us to keep looping until all sorted.
    while in_order:
        # Assume the 2 elements we look at in each cycle aren't in order
        in_order = False
        # Loop through all list elements (we access i+1, so len-1)
        for i in range(len(num_list) - 1):
            # If the element is greater than the element after, do this:
            if num_list[i] > num_list[i + 1]:
                # Swap the 2 elements
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                # Reset as True so that we can continue through the loop
                in_order = True
    # Final return true
    return True


# Test case - make a list of unordered nums
list_of_nums = [7,6,5,4,3,2,8,9,1,2,3,4,5,6]
# Enact the function and print it
bubble(list_of_nums)
print(list_of_nums)

