# << Swami Shreeji >>
# @nishantpatel
# Mask email and phone number according to the rules

# E:jackAndJill@gmail.com  					    	# E:j*****l@gmail.com
# P:(333)456-7890 				OUTPUT:			# P:***-***-7890
# P:+1(333) 456-7890 							# P:+*-***-***-7890

import sys

# Process email

while True:
	testInput = raw_input()
	
	if testInput == "":
		break

	# Process email
	elif testInput.startswith("E:"):
		userName = testInput[2:testInput.find("@")]
		domainName = testInput[testInput.find("@"):]
		stars = "*" * 5
		
		userMasked = userName[0] + stars + userName[-1:] + domainName
		print "E:" + userMasked

	# Process phone number
	elif testInput.startswith("P:"):
		start = testInput[2:-4]
		mask = "***-***-"
		lastFour = testInput[-4:]

		start = start.translate(None, "()- " )

		if len(start) == 6:
			ans = mask
		elif len(start) == 8:
			ans = "+*-" + mask
		elif len(start) == 9:
			ans = "+**-" + mask
		elif len(start) == 10:
			ans = "+***-" + mask

		print "P:" + ans + lastFour
