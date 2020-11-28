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
out_file_name = 'summary_analysis.csv'
out_csvpath = os.path.join(out_path, out_file_name)

# Get number of votes per candidate
def candidateVoteCount(candidate, names):

	votes = 0 

	for name in names:
		if candidate == name:
			votes += 1

	return votes

with open(in_csvpath, 'r') as inFile:

	# Create reader obj for election data and skip header/field row 
	election_data = csv.reader(inFile, delimiter=',')
	header = next(election_data)

	total_votes = 0
	candidates = []
	votes_per_candidate = []
	name_instances = []

	# Gets count of total number of votes, all name instances, and unique instances
	# of each candididate 
	for vote in election_data:
		total_votes += 1 
		name_instances.append(vote[2])
		if vote[2] not in candidates:
			candidates.append(vote[2])

	# Call to get votes per candidate 
	for candidate in candidates:
		votes_per_candidate.append(candidateVoteCount(candidate, name_instances))
		

	# Summary 
	print('Election Results')
	print('--------------------------')
	print('Total Votes: ', total_votes)
	print('--------------------------')

	for candidate in candidates:
		candidate_index = candidates.index(candidate)
		votes_recieved = votes_per_candidate[candidate_index] 

		percent_votes = format(100 * (votes_recieved / total_votes), '.2f')
		print(candidate, ': ', percent_votes, '% (', votes_recieved, ')')

	print('--------------------------')
	winner_index = votes_per_candidate.index(max(votes_per_candidate))
	winner = candidates[winner_index]
	print('Winner: ', winner)
	print('--------------------------')

with open(out_csvpath, 'w', newline='') as OutFile:

	# Write analysis to .csv
	summary = csv.writer(OutFile, delimiter=',')

	summary.writerow(['Election Results'])
	summary.writerow(['--------------------------'])
	summary.writerow(['Total Votes', total_votes])
	summary.writerow(['--------------------------'])
	summary.writerow(['','Percent of Votes(%)', 'Number of Votes'])

	for candidate in candidates:
		candidate_index = candidates.index(candidate)
		votes_recieved = votes_per_candidate[candidate_index] 

		percent_votes = round(100 * (votes_recieved / total_votes), 3)
		summary.writerow([candidate, percent_votes, votes_recieved])

	summary.writerow(['--------------------------'])
	summary.writerow(['Winner', winner])
	summary.writerow(['--------------------------'])