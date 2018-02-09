# Swami Shreeji
# 8 Feb 2018

# Given an array of integers, every element appears twice except for one. Find which one

def singleNum(numbers):
	tracker = {}

	for elem in numbers:
		if elem in tracker:
			tracker.pop(elem)
		else:
			tracker[elem] = "Distinct"

	for elem in tracker:
		if tracker.get(elem) == "Distinct":
			print elem


numbers = [5, 5, 3, 3, 8, 8, 9, 9, 0, 0, 1, 1, 2, 2, 7, 4, 4]
singleNum(numbers)
