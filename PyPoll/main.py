import csv
import os
from collections import Counter
csvpath = os.path.join('raw_data', 'election_data_2.csv')
candidate_list = []
row_count = 0

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        row_count = row_count + 1
        candidate_list.append(row[2])
    candidate_count = Counter(candidate_list)

print("Election Results")
print("-----------------------------------")

print("Total Votes: " + str(row_count))
print("-----------------------------------")
for item in candidate_count:
    print(item + ": " +  str(((candidate_count[item]/row_count)*100)) + "% (" + str(candidate_count[item]) + ")")
print("-----------------------------------")
print("Winner: " + max(candidate_count))
print("-----------------------------------")





        