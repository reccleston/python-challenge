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
	profits = []
	changes = []

	for month, profit in budget_sheet:
		total_months += 1
		net += int(profit)
		profits.append(int(profit))

	for month_num, profit in enumerate(profits):
		print(profits[month_num + 1])
		print(profits[month_num])
		change = profits[month_num + 1] - profits[month_num]
		print('change: ', change)
		changes.append(change)

	print('~*~*~*~')
	print(changes)
	# budget_sheet = csv.reader(inFile, delimiter=',')
	# header = next(budget_sheet)

	# total_months = 0
	# net = 0
	# change = 0
	# current_month = ''

	# for current_month, current_profit in budget_sheet:
	# 	total_months += 1
	# 	net += int(current_profit)
	# 	print(current_month)
	# 	print(current_profit)
		

	# print(total_months)
	# print(net)


	

