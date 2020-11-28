# 
# PyPoll
# Ryan Eccleston-Murdock
# 28 November 2020 
# 
# Purpose: Determine stats for an election 
# Sources: 

import os
import csv

in_path = 'Resources'
in_file_name = 'election_data.csv'
in_csvpath = os.path.join(in_path, in_file_name)

out_path = 'analysis'
out_file_name = ''
out_csvpath = os.path.join(out_path, out_file_name)

def candidateVoteCount(candidate, data):

	votes = 0 
	print(candidate)
	for vote in data:
		print(vote)
		if candidate == vote[2]:
			votes += 1

	return votes

with open(in_csvpath, 'r') as inFile:

	election_data = csv.reader(inFile, delimiter=',')
	header = next(election_data)

	total_votes = 0
	candidates = []

	for vote in election_data:
		total_votes += 1 
		if vote[2] not in candidates:
			candidates.append(vote[2])

	for candidate in candidates:
		print(candidateVoteCount(candidate, election_data))
		



	print('Total Votes: ', total_votes)
	print(candidates)