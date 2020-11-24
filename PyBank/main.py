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
import string 
import random

path = 'Resources'
csvpath = os.path.join(path, 'budget_data.csv')

with open(csvpath, 'r') as inFile:

	budget_sheet = csv.reader(inFile, delimiter=',')
	next(budget_sheet)

	total_months = 0
	net = 0
	current_month = ''
	
	for row in budget_sheet:
		total_months += 1
		net += int(row[1])

	print(total_months)
	print(net)