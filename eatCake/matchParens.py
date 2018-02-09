# Swami Shreeji
# 8 Feb 2018

# Given a sentence and an integer pointing to an open parenthesis, 
# returns the matching closing parenthesis index

def matchingParen(sentence, parenPos):
	openCount = 0
	position = parenPos + 1

	while position <= len(sentence) - 1:
		char = sentence[position]

		if char == '(':
			openCount += 1
		elif char == ')':
			if openCount == 0:
				return position
			else:
				openCount -= 1
		position += 1


sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
parenPos = 10

soln = matchingParen(sentence, parenPos)
print soln
