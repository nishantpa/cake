# << Swami Shreeji >>
# 4 Jan 2018

# You have a list of integers, and for each index you want to find the product
#   of every integer except the integer at that index. Write a function 
#   get_products_of_all_ints_except_at_index() that takes a list of integers 
#   and returns a list of the products. 

	# Given:
	# [1, 7, 3, 4]

	# your function would return:
	# [84, 12, 28, 21]

	# by calculating:
	# [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
	
'''
	import numpy as np 
	def get_products_of_all_ints_except_at_index(raw = []):
		# Find the product when all elems in list are multiplied together
		prod = np.prod(raw)
		
		# Divide out the unneeded element
		result = []
		for elem in raw:
			subAns = prod / elem
			result.append(subAns)

		return result 

	case1 = [1, 7, 3, 4]
	answer = get_products_of_all_ints_except_at_index(case1)
	print answer
'''

# Now, redo question and DO NOT DIVIDE

def get_products_of_all_ints_except_at_index(intList = []):
	
	prodSoFar = 1
	prodOfAll_NotCurrent = []
	
	for elem in intList:
		prodOfAll_NotCurrent.append(prodSoFar)
		prodSoFar *= elem

	# Note that reversed does NOT create a new list. It returns an iterator
	prodSoFar = 1
	
	i = len(intList) - 1
	while i >= 0:
		prodOfAll_NotCurrent[i] *= prodSoFar
		prodSoFar *= intList[i]
		i -= 1

	print prodOfAll_NotCurrent


case1 = [3, 1, 2, 5, 6, 4]
answer = get_products_of_all_ints_except_at_index(case1)
