# Swami Shreeji
# 29 Jan 2018
# HOW TO RUN: python rotationPoint.py in terminal

# I want to learn some big words so people think I'm smart.

# I opened up a dictionary to a page in the middle and started flipping through, 
# looking for words I didn't know. I put each word I didn't know at increasing 
# indices in a huge list I created in memory. When I reached the end of the 
# dictionary, I started from the beginning and did the same thing until I reached
#  the page I started at.

# Now I have a list of words that are mostly alphabetical, except they start 
# somewhere in the middle of the alphabet, reach the end, and then start from the 
# beginning of the alphabet. In other words, this is an alphabetically ordered 
# list that has been "rotated." 

# Write a function for finding the index of the "rotation point," which is 
# where I started working from the beginning of the dictionary.


# ATTACK PLAN: Binary search on words. It'll be an altered binary search  

def find_rotation_point(wordsList):
    first_word = wordsList[0]
    floor_index = 0
    ceiling_index = len(wordsList) - 1

    while floor_index < ceiling_index:
        guess_index = floor_index + ((ceiling_index - floor_index) / 2)

        # If guess comes after first word or is the first word
        if wordsList[guess_index] >= first_word:
            # Go right
            print
            print "Going right"
            print "floor_index: ", floor_index, wordsList[floor_index]
            floor_index = guess_index
        else:
            # Go left
            print
            print "Go left"
            print "ceiling_index: ", ceiling_index, wordsList[ceiling_index]
            ceiling_index = guess_index

        # If floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            print 
            print "floor and ceiling converge"
            print "floor_index: ", floor_index, "ceiling_index: ", ceiling_index, wordsList[ceiling_index] 
            return ceiling_index
	


# 13 words
wordsList = [
   'ptolemaic'
  ,'patel'
  ,'retrograde'
  ,'supplant'
  ,'the'
  ,'undulate'
  ,'xenoepist'
  ,'asymptote' # <-- rotates here!
  ,'babka'
  ,'banoffee'
  ,'engender'
  ,'karpatka'
  ,'othellolagkage'
  ,
]

find_rotation_point(wordsList)
