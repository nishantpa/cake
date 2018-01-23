# << Swami Shreeji >>
# 8 Jan 2018, 9 Jan 


''' Finding the length of a sublist '''
# myList = [ 
# 		   ["hi", "djh3"],
# 		   ["1"], 
# 		   ["jdw", "exw", "dw4d", "cwrwr", "rxwcrw"] 
# 		 ]
# print len(min(myList))



''' Example of reading stdIn/user input '''
# import sys

# def printArgs(args):
#     print "THe user input the following: "
#     for arg in args:
#         print arg
        
# inputList = []
# while True:
# 	userInput = raw_input()
# 	if userInput == "":
# 		break
# 	else:
# 		inputList.append(userInput)

# printArgs(inputList)


# case1 = [10, 7, 11, 8, 5, 9]
# lowestValueIndex = case1.index( min(case1) )
# print lowestValueIndex


''' Playing with Hashes '''
import hashlib
print (hashlib.algorithms_available)

# Before hashing, need the string in  bytes
myString = "Hello world"
hashMyString = hashlib.md5(myString.encode())
print hashMyString