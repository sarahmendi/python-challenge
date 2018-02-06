import csv
import os
from collections import Counter
csvpath = os.path.join('raw_data', 'budget_data_1.csv')
#candidate_list = []
#row_count = 0

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #next(csvreader, None)
    print(csvreader)