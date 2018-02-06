import csv
import os

csvpath = os.path.join('raw_data', 'employee_data1.csv')
empid = []
name = []
dob = []
ssn = []
state = []
first_name = []
last_name = []

state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
    'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY',
}

with open(csvpath, newline= "") as csv_infile:
    csvreader = csv.reader(csv_infile, delimiter = ",")
    next(csvreader, None)

    for row in csvreader:

        empid.append(row[0])

        name = row[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])

        dob_date = row[2].split("-")
        new_dob = dob_date[1] + "/" + dob_date[2] +"/" + dob_date[0]
        dob.append(new_dob)

        ssn_stars = row[3].split("-")
        new_ssn = "***-***" + ssn_stars[2]
        ssn.append(new_ssn)

        state.append(state_abbrev)

employees = zip(empid, first_name, last_name, dob, ssn, state)
new_csvpath = os.path.join('raw_data', 'mainpy.csv')
        
with open(new_csvpath, 'w', newline="") as csv_outfile:
    csvwriter=csv.writer(csv_outfile, delimiter = ",")
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", " DOB", "SSN", "State"])
    
    for employee in employees:
        csvwriter.writerow(employee)