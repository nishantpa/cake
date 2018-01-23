# << Swami Shreeji >>
# @nishanpatel ; 13 Oct 2017
# HackerRank CamelCase Challenge - Algorithms --> Strings --> CamelCase

import sys
import string

# Take test input
testInput = raw_input()
numWords = len(filter(lambda x: x in string.uppercase, testInput)) + 1

print numWords