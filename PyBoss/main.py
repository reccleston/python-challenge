# 
# PyBoss
# Ryan Eccleston-Murdock
# 28 November 2020 
# 
# Purpose: Convert old employee records into the new format.
#
# Sources: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5

import os
import csv
import datetime 

in_path = './'
in_file_name = 'employee_data.csv'
in_csvpath = os.path.join(in_path, in_file_name)

out_path = 'updated_employee_record'
out_file_name = 'updated_employee_record.csv'
out_csvpath = os.path.join(out_path, out_file_name)

ids = []
first_name = []
last_name = []
dob = []
ssn = []
states = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

def format_states(states):

	for state in states:
		employee = states.index(state)
		states[employee] = us_state_abbrev[state]

def format_ssn(ssn):

	for ss in ssn:
		formated_ssn = '***-**-'
		employee = ssn.index(ss)
		for number in range(7,11):
			formated_ssn += ss[number]
		ssn[employee] = formated_ssn

def format_dob(dob):

	for birthday in dob:
		employee = dob.index(birthday)
		fomrated_dob = datetime.datetime.strptime(birthday, '%Y-%m-%d').strftime('%m/%d/%y')	
		dob[employee] = fomrated_dob

with open(in_csvpath, 'r') as inFile:

	employee_records_old = csv.reader(inFile, delimiter=',')
	header = next(employee_records_old)

	for employee in employee_records_old:
		ids.append(employee[0])

		first = employee[1].split()[0]
		last = employee[1].split()[1]

		first_name.append(first)
		last_name.append(last)

		dob.append(employee[2])
		ssn.append(employee[3])
		states.append(employee[4])

	format_dob(dob)
	format_ssn(ssn)
	format_states(states)

with open(out_csvpath, 'w', newline='') as outFile:

	summary = csv.writer(outFile, delimiter=',')

	summary.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

	for row in range(len(ids)):
		summary.writerow([ids[row], first_name[row], last_name[row], dob[row], ssn[row], states[row]])


	