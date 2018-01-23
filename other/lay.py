# Swami Shreeji 
# @nishantpatel ; 5 Dec 2017
# Write a function that accepts 2 args. arg1 is an multiDim array of numbers
	# and arg2 is a number. Find the row that whos sum is closest to arg2

import sys
import numpy as np

def getRow(case, target):
	# Sum up individual rows
	i = 0
	result = []
	while i != len(case):
		result.append( sum(case[i]) )
		i += 1

	# Find the actual distance from target
	filtResult = []
	j = 0
	while j != len(result):
		filtResult.append( abs(result[j] - target) )
		j += 1

	# Get first occurence index of row with solution
	minIndex = filtResult.index( min(filtResult) )
	solution = np.asarray(case[minIndex])
	return solution


# Test cases
case1 = [[1,3,6], [2,7,1], [5,2,8]]
target1 = 10

case2 = [[1,3,6,-8], [2,7,1,0], [4,5,2,8], [2,3,7,10]]
target2 = 9


# Function returns row as numpy array 
solution = getRow(case2, target2)
print solution