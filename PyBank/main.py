import csv
import os
from collections import Counter
csvpath = os.path.join('raw_data', 'budget_data_1.csv')
month = []
revenue = []
total_revenue = 0
avg_change = []
greatest_increase = []
greatest_decrease = []
row_count = 0

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    #print(csvreader)

    for row in csvreader:
        #print(row)
        row_count = row_count + 1
        month.append(row[0])
        month_count = Counter((row[0].split("-")))
        month.append(month_count[0])
        revenue.append(row[1])
        total_revenue = total_revenue + int(row[1])
        avg_change = round((total_revenue / row_count),2)

       
    


print("Financial Analysis")
print("-----------------------------------")

print("Total Months: " + str(month_count))   

print("Total Revenue: $" + (str(total_revenue)))

print("Average Revenue Change: $" + (str(avg_change)))

print("Greatest Increase in Revenue: " + str(month_count) + " ($" + (str(greatest_increase)) + ") ")

print("Greatest Decrease in Revenue: " + str(month_count) + " ($" + (str(greatest_decrease)) + ") ")
