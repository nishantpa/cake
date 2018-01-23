# << Swami Shreeji >>
# 21 Nov 2017
# Algo --> Implementation --> Encryption

import sys
import string
import math

# Cases
case0 = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots" # 54 PASS
case1 = "haveaniceday" # 12 PASS 
case2 = "feedthedog" # 10 PASS
case3 = "chillout" # 8 FAILS

def encrypt(args):
	# Step 1: Remove all whitespace
	args = args.replace(" ","")
	argsLen = len(args)

	# Prelim setup
	cols = 0
	rows = int (math.floor(math.sqrt(argsLen)))
	if rows * rows <= argsLen:
		cols = rows + 1

	# Define rect dimensions
	rect = [["" for x in range(rows)] for x in range(cols)]

	# Step 2: Build rect
	colNum = 0 ; rowNum = 0
	while True:
		for char in args:
			rect[colNum][rowNum] = char
			colNum += 1
			
			if colNum == cols:
				rowNum += 1
				colNum = 0

		# Filter it. Ugly but works ... Come back to this
		antiSol = (', '.join(map(str, rect)))
		antiSol = antiSol.replace("],", "|")
		antiSol = antiSol.translate(None, '[,\'] ')
		antiSol = antiSol.replace("|", " ")

		print antiSol
		break

encrypt(case0)	
encrypt(case1)	
encrypt(case2)	
# encrypt(case3) FAILS HERE	
