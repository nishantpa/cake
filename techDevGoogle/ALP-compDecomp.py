# << Swami Shreeji >>
# @nishantpatel ; 21 Nov 2017
# Google's Tech Dev Guide - Former Coding Interview Question
	# Compression and Decompression

# Test Cases & output:
# 3[abc]4[ab]c		--> abcabcabcababababc 	[PASSES]
# 2[3[a]b]			--> aaabaaab 			[PENDING]

import sys
import string

# Test cases | Interpretted as a tuple
case1 = "10[abc]4[ab]c"
case2 = "2[3[a]b]"

def decompress(args):
	# General Case
	currString = ""
	currInt = ""
	repeater = 0

	for char in args:
		if char.isdigit():
			currInt = currInt + char
		elif char.isalpha():
			currString = currString + char
		elif char == "]":
			repeater = int (currInt)
			for i in range(0, repeater):
				sys.stdout.write(currString)
			currString = ""
			currInt = "" 
	sys.stdout.write(currString)

decompress(case1)
print ""