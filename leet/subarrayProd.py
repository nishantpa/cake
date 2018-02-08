# Swami Shreeji
# 7 Feb 2018
# Speedrun - 10 min hackerrank challenge

# You're passed an array of integers. Your task is to find all the subarrays
# you can make with that integer, and find the product. After finding the product
# check to see which products are less than some value k. Return the count of 
# how many of those subarray products are less than k.

import itertools
from operator import mul 

temp = []
def count(numbers, k):
    i = 0
    subarrays = []
    while i < len(numbers):
        j = 3
        while j > 0:
            temp = numbers[i:j]
            subarrays.append(temp)
            j -= 1
        i += 1
    
    parseThis = []
    for elem in subarrays:
        if len(elem) > 0:
            parseThis.append(elem)
    
    almostThere = []
    for elem in parseThis:
        if reduce (mul, elem, 1) < k:
            almostThere.append(elem)
    return len(almostThere)