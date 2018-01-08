# << Swami Shreeji >>
# 8 Jan 2017

# A straightforward implementation of quicksort. 

def quickSort(myArray):
	# Base case: empty or only 1 item
	if len(myArray) < 2:
		return myArray
	else:
		pivot = myArray[0]

		# Partition array into 2: smaller and larger compared to pivot
		less = [i for i in myArray[1:] if i < pivot]
		greater = [i for i in myArray[1:] if i > pivot]

		# Recursively sort a smaller problem until it's sorted completely
		return quickSort(less) + [pivot] + quickSort(greater)

myArray = [10, 5, 2, 3, 1, 6, -2]
print quickSort(myArray)