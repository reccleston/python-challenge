# 
# PyBank 
# Ryan Eccleston-Murdock
# 28 November 2020 
# 
# Purpose: Analyze .csv financial data 

import os
import csv
import string 
import random

path = 'Resources'
csvpath = os.path.join(path, 'budget_data.csv')

with open(csvpath) as inFile:
	budget_sheet = csv.reader(inFile, delimiter=',')

	total_months = sum(1 for row in budget_sheet) - 1
	print(total_months)
	print('milk')
	# header = next(budget_sheet)

	net = 0
	for row in budget_sheet:
		print(row)
