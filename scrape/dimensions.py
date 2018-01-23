# @nishantpatel ; July 28, 2017
# IA - 62: Car dimensions
# Target files and script located in same dir

import sys

for args in sys.argv:
	from bs4 import BeautifulSoup
	with open(args) as fp:
	    soup = BeautifulSoup(fp, "html.parser")

	for vehicleDetails in soup.find_all(class_="unit"):
	    print vehicleDetails.text.encode('utf-8').split('L ')[0],
	    print ",",  
	    print vehicleDetails.text.encode('utf-8').replace(" ", "").split('H:')[1][0:14].replace("x", ",")

	# To separate companies
	print