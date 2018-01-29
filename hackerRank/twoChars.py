# << Swami Shreeji >>
# @nishantpatel ; 16 Oct 2017, 20 Dec 2017 COMPLETE
# Algorithms --> Strings --> twoChars beabeefeab
# Test case1: beabeefeab
# Test case28: tlymrvjcylhqifsqtyyzfaugtibkkghfhyzxqbsizkjguqlqwwetyofqihtpkmpdlgthfybfhhmjerjdkybwppwrdapirukcshkpngayrdruanjtziknnwxmsjpnuswllymhkmztsrcwwzmlbcoakswwffveobbvzinkhnmvwqhpfednhsuzmffaebi

import sys
import collections
from itertools import combinations
import string

testStrLen = raw_input()
testStr = raw_input()

# Extract unique chars
testStrInfo = collections.Counter(testStr)
uniqueLetters = list(testStrInfo)

# Get all pair combos
storeCombos = list()
for pair in combinations(uniqueLetters, 2):
	 pairedUp = pair[0] + pair[1]
	 storeCombos.append(pairedUp)

# Produce all possible strings of 2 unique letters from testStr
# Not all of these conform to the answer
storePotentialStrings = list()
for elem in storeCombos:
	result = ''.join(c for c in testStr if c == (elem[0]) or c == (elem[1]))
	storePotentialStrings.append(result)

# Remove illegal strings from storePotentialAnswers
temp = ""
for elem in storePotentialStrings:
	for char in elem[1:]:
		if temp == char:
			print elem, 
			storePotentialStrings.remove(elem)
			break
		else:
			temp = char

# Print answer. Remove len to get element
print len( max(storePotentialStrings, key=len) )