# << Swami Shreeji >>
# 8 Jan 2018

# Inflight Entertainment.
# You've built an inflight entertainment system with on-demand movie streaming.

# Users on longer flights like to start a second movie right when their first one ends, 
# but they complain that the plane usually lands before they can see the ending. So 
# you're building a feature for choosing two movies whose total runtimes will equal 
# the exact flight length.

# Write a function that takes an integer flight_length (in minutes) and a 
# list of integers movie_lengths (in minutes) and returns a boolean indicating 
# whether there are two numbers in movie_lengths whose sum equals flight_length.

# When building your function:

# Assume your users will watch exactly two movies
# Don't make your users watch the same movie twice
# Optimize for runtime over memory

import random

def entertainment(flightTime, movieTime_List):
	timeOfFirstMovie = random.choice(movieTime_List)
	timeofSecondMovie = flightTime - timeOfFirstMovie

	# To protect from someone watching the same movie over
	movieTime_List.remove(timeOfFirstMovie)

	determineSecondMovie = set(movieTime_List)
	if timeofSecondMovie in determineSecondMovie:
		# print "Success"
		return True
	else:
		# print "Fail"
		return False


flightTime = 120
movieLengths = [i for i in xrange(47,101)]

entertainment(flightTime, movieLengths)
