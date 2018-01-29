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

def rotationPoint (wordsList):
	print wordsList


words = [
  'ptolemaic',
  'retrograde',
  'supplant',
  'undulate',
  'xenoepist',
  'asymptote',  # <-- rotates here!
  'babka',
  'banoffee',
  'engender',
  'karpatka',
  'othellolagkage',
]

rotationPoint(words)