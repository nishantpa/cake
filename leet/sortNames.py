# Swami Shreeji
# 7 Feb 2018

# Sorting names, instead of numbers. And get the most frequent name at the start

def sortNames(names):
	# Check if in dict, increment if yes. Else, add to dict
	myDict = {}
	for elem in names:
		if elem in myDict:
			myDict[elem] += 1
		else:
			myDict[elem] = 1

	# Reverse sort and return based on values
	return sorted(myDict.items(), key = lambda x: x[1], reverse = True)


names = ["Nishant", "Anand", "Anand", "Atmiya", "Atmiya", "Atmiya", "Lallu", "Sahaj", "Sahaj", "Sahil", "Hariprasad"]
soln = sortNames(names)
print soln

