# << Swami Shreeji >>
# @nishantpatel ; 23 Nov 2017, 27 Nov 2017
# TASK: Using 2016_general.csv
# 	Get the candidate with the most votes. DONE
# 	Get the votes of all candidates who ran for president and vp DONE

import csv
import sys
from collections import defaultdict

# Read once, power away after
def preWork():
	# Holds OFFICE, CANDIDATE and VOTES. Dups exist
	data = []
	with open('2016_general.csv') as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	        candAndVotes = [row['OFFICE'], row['CANDIDATE'], int (row['VOTES'])] 
	        data.append(candAndVotes)
	return data

# Return candidate with most votes
def mostVoted(args):
	result = defaultdict(int)
	for item in args:
		office, cand, votes = item
		result[(cand)] += votes

	# print dict(result)
	mostVotedCand = max(result, key=result.get)
	print mostVotedCand

# Get the votes of all candidates who ran for president
def pAndVPVotes(args):
	result = defaultdict(int)
	for item in args:
		if item[0] == 'PRESIDENT AND VICE PRESIDENT OF THE UNITED STATES':
			office, cand, votes = item
			result[(cand)] += votes

	print dict(result)


csvData = preWork()
mostVoted(csvData)
pAndVPVotes(csvData)
