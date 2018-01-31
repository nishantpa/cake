# Swami Shreeji
# You cannot use the same element twice

# This is assuming all numbers are +
def twoSum(myList, target):
	targetIndices = []

	for elem in myList:
		searchFor = abs(elem - target)
		if searchFor in myList[myList.index(elem) + 1:]:
			targetIndices.append(myList.index(elem))
			targetIndices.append(myList.index(searchFor))
			break

	print targetIndices

# Test cases
# case1 = [2, 7, 11, 15]; target = 9
case2 = [3, 2, 4]; target = 6
twoSum(case2, target)
