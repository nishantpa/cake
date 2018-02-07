# Swami Shreeji
# 7 Feb 2018

# Determine whether a string is a "lovely" string, meaning its characters are not repeated. 
# i.e. 123 is lovely, but nishant is not

# NOTE: The answer is function is case sensitive. Add a lowercase if needed, use a set

def lovely(case):
	answer = {}
	for elem in case:
		if len(set(elem)) == len(elem):
			answer[elem] = True
	return answer

# Prepopulate case with numbers
case = ["nishant", "Hariprasad", "Jasmine", "33", "Swami"]
lovely = lovely(case)

print lovely
