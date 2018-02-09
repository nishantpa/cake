# Swami Shreeji 
# 9 Feb 2018

# Reverse string

import sys

case = "Hello, world!"

i = len(case) - 1
while i >= 0:
	sys.stdout.write(case[i]) 
	i -= 1
print
