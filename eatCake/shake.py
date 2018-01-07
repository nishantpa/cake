# << Swami Shreeji >>
# 7 Jan 2018
# TASK: Using 2016_general.csv
# 	Get the candidate with the most votes.
# 	Get the votes of all candidates who ran for president and vp 

# NOTE: The csv data is raw. This means duplicates of candidates exist.
#  But those duplicates will have some differences - like votes across rows

import csv
from collections import defaultdict

# Reading from CSV
def prework():
	# Holds OFFICE, CANDIDATE, and VOTES. Dups exist
	data = []
	with open('2016_general.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			office_Cand_Votes = [ row['OFFICE'], row['CANDIDATE'], int (row['VOTES']) ]
			data.append(office_Cand_Votes)
	return data

# Return candidate with highest votes
def mostVoted(csvData):
	result = defaultdict(int)

	# Iterate through all items in csvData and sum candidate's votes. This
	#  ensures that we can sum up votes for that candidate from other rows
	for item in csvData:
		office, candidate, votes = item
		result[candidate] += votes

	mostVotedCandidate = max(result, key = result.get)
	return mostVotedCandidate

def pAndVPVotes(csvData):
	result = defaultdict(int)
	for item in csvData:
		if item[0] == 'PRESIDENT AND VICE PRESIDENT OF THE UNITED STATES':
			office, candidate, votes = item
			result[candidate] += votes

	return dict(result)

csvData = prework()
mostVotedCandidate = mostVoted(csvData)
candsFor_P_VP = pAndVPVotes(csvData)

print mostVotedCandidate
print candsFor_P_VP
