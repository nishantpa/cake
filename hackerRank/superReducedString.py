# << Swami Shreeji >>
# @nishantpatel; 12 Sep 2017, 21 Nov 2017
# HackerRank String Challenge: Super reduced string

import sys

# Test cases
	# str1 = "aabcc" # --> b
	# str2 = "baab" # --> EMPTY STRING
	# str3 = "aaabccddd" # --> abd
	# case11 = "acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj" # ANS: acdqgacdqj
	# case13 = "lrfkqyuqfjjfquyqkfrlkxyqvnrtyssytrnvqyxkfrzrmzlygffgylzmrzrfveulqfpdbhhbdpfqluevlqdqrrcrwddwrcrrqdql" # ANS: Empty String
	# case14 = "oagciicgaoyjmahhamjymmwjnnjwmmvpxhpphxpvlikappakilyygvkkvgyymlpfddfplmhiodvvdoihfxpkggkpxfuevvuuvveu" # ANS: Empty String

str4 = raw_input()

# Save the char just read into var
saveChar = ""

def reduceString(testStr, saveChar):
	for char in testStr:
		if saveChar == char:
			testStr =  testStr.replace(saveChar + char, "")
		else:
			saveChar = char
	return testStr

# Print final answer
while str4 != "" :
	str4 = reduceString(str4, saveChar)
	if str4 == reduceString(str4, saveChar) and str4 != "":
		print str4
		break
	elif str4 == "":
		print "Empty String"
		break