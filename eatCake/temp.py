# << Swami Shreeji >>
# 8 Jan 2018

# Just checking ... 



# myList = [ 
# 		   ["hi", "djh3"],
# 		   ["1"], 
# 		   ["jdw", "exw", "dw4d", "cwrwr", "rxwcrw"] 
# 		 ]
# print len(min(myList))


import sys

def printArgs(args):
    print "THe user input the following: "
    for arg in args:
        print arg
        
inputList = []
while True:
	userInput = raw_input()
	if userInput == "":
		break
	else:
		inputList.append(userInput)

printArgs(inputList)
