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

path = 'Resources'
file_name = 'budget_data.csv'
csvpath = os.path.join(path, file_name)

with open(csvpath, 'r') as inFile:

	budget_sheet = csv.reader(inFile, delimiter=',')
	header = next(budget_sheet)

	total_months = 0
	net = 0 
	months = []
	profits = []
	changes = []

	for month, profit in budget_sheet:
		total_months += 1
		net += int(profit)
		months.append(month)
		profits.append(int(profit))

	for i in range(len(profits) - 1):
		change = profits[i + 1] - profits[i]
		changes.append(change)

	average_change = sum(changes) / len(changes)

	great_increase = max(changes)
	great_increase_month = changes.index(great_increase)

	great_decrease = min(changes)
	great_decrease_month = changes.index(great_decrease)

	print('Financial Analysis')
	print('--------------------------')
	print('Total months: ', total_months)
	print('Total: $', net)
	print('Average Change: $', round(average_change, 2))
	print('Greatest Increase in Profits: ', months[great_increase_month], '($', great_increase, ')')
	print('Greatest Decrease in Profits: ', months[great_decrease_month], '($', great_decrease, ')')
	print('--------------------------')

