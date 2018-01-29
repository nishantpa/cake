# Swami Shreeji
# Bracket validator - leetcode

# Given a string containing just the characters 
# '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# The brackets must close in the correct order, 
# "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

def validator(case):
	validatorStack = []
	
	if not validatorStack:
		validatorStack.append(case[0])
	try:
		for char in case[1:]:
			if char == ')':
				leftParen = validatorStack.pop()
				if leftParen != '(':
					print "Unbalanced!: ", leftParen
					return
			
			elif char == '}':
				leftBrace = validatorStack.pop()
				if leftBrace != '{':
					print "Unbalanced!: ", leftBrace
					return

			elif char == ']':
				leftBracket = validatorStack.pop()
				if leftBracket != '{':
					print "Unbalanced!: ", leftBracket
					return

			else:
				validatorStack.append(char)

	except IndexError:
		print "Unbalanced! IndexError is evidence."


case0 = "()"
case1 = "())"
case2 = "()[]{}"
case3 = "(]"
case4 = "([)]"

validator(case1)
