# << Swami Shreeji >>
# @nishantpatel; 21 Nov 2017
# HackerRank String Challenge: Super reduced string
# Another solution found on github

#!/bin/python

import sys

s = raw_input()
stack = []
for i in xrange(len(s)):
    if not stack or s[i] != stack[-1]:
        stack += [s[i]]
    else:
        stack.pop()
if stack:
    print ''.join(stack)
else:
    print 'Empty String'