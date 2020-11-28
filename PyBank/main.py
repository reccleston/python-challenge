# 
# PyBank 
# Ryan Eccleston-Murdock
# 28 November 2020 
# 
# Purpose: Analyze .csv financial data 
#
# Sources: 

import os
import csv

in_path = 'Resources'
in_file_name = 'budget_data.csv'
in_csvpath = os.path.join(in_path, in_file_name)

out_path = 'analysis'
out_file_name = 'financial_summary.csv'
out_csvpath = os.path.join(out_path, out_file_name)

with open(in_csvpath, 'r') as inFile:

	# Create reader obj for budget data and skip header/field row 
	budget_sheet = csv.reader(inFile, delimiter=',')
	header = next(budget_sheet)

	total_months = 0
	net = 0 
	months = []
	profits = []
	changes = []

	# Gets count of total number of months, net profit/loss and months/profit 
	# pairs 
	for month, profit in budget_sheet:
		total_months += 1
		net += int(profit)
		months.append(month)
		profits.append(int(profit))

	# Get month to month change 
	for i in range(len(profits) - 1):
		change = profits[i + 1] - profits[i]
		changes.append(change)

	# Gets average change over period
	average_change = sum(changes) / len(changes)

	# Gets extrema
	great_increase = max(changes)
	great_increase_month = changes.index(great_increase)

	great_decrease = min(changes)
	great_decrease_month = changes.index(great_decrease)

	# Summary 
	print('Financial Analysis')
	print('--------------------------')
	print('Total months: ', total_months)
	print('Total: $', net)
	print('Average Change: $', round(average_change, 2))
	print('Greatest Increase in Profits: ', months[great_increase_month], '($', great_increase, ')')
	print('Greatest Decrease in Profits: ', months[great_decrease_month], '($', great_decrease, ')')
	print('--------------------------')

with open(out_csvpath, 'w', newline='') as outFile:

	# Write analysis to .csv
	summary = csv.writer(outFile, delimiter=',')

	summary.writerow(['Financial Analysis'])
	summary.writerow(['--------------------------'])
	summary.writerow(['Total months', total_months])
	summary.writerow(['Total', net])
	summary.writerow(['Average Change', round(average_change, 2)])
	summary.writerow(['Greatest Increase in Profits', months[great_increase_month], great_increase])
	summary.writerow(['Greatest Decrease in Profits', months[great_decrease_month], great_decrease])
	summary.writerow(['--------------------------'])

	
