#first step is to read CVS in order to work with the file
#import os will allow us to creat file paths across operating systems

import os

#import module for reading CVS files
import csv

#set the path to open the file
csvpath = os.path.join('budget_data.csv')

print(csvpath)

#generate count_month for counting rows since each row is a month
count_month = 0
total  = 0 
profit_loses = []
date = []




#read CSV module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader: 
        print (row)
        count_month = count_month + 1
        total += float(row[1])
        total_format = '${:,.2f}'.format(total)
        profit_loses.append(int(row[1]))
        date.append(row[0])
        
      
delta_change = 0
greatest_increase = (profit_loses[1] - profit_loses[0])
greatest_decrease = (profit_loses[1] - profit_loses[0])

for i in range(0,len(profit_loses)):
    if i >= 1:
        delta_change += (profit_loses[i] - profit_loses[i-1])
    if greatest_increase <= (profit_loses[i] - profit_loses[i-1]): 
        greatest_increase = (profit_loses[i] - profit_loses[i-1])
        date_greatest_increase = date[i]
    if greatest_decrease >= (profit_loses[i] - profit_loses[i-1]):
        greatest_decrease = (profit_loses[i] - profit_loses[i-1])
        date_greatest_decrease = date[i]

average_change = delta_change/(count_month-1)

round_average_change = round(average_change, 2)

total_average = '${:,.2f}'.format(round_average_change)

format_greatest_increase = '${:,.2f}'.format(greatest_increase)

format_greatest_decrease = '${:,.2f}'.format(greatest_decrease)




results = os.path.join("pybankanalysis.txt")

print(results)

with open(results,"w") as analysis:
    analysis.write("Financial Analysis")
    analysis.write(" ")
    analysis.write("-----------------------")
    analysis.write(" ")
    analysis.write("Total Months: " + str(count_month))
    analysis.write("Total: " + str(total_format))
    analysis.write("Average Change: " + str(total_average))
    analysis.write("Greatest Increase in Profits: " + "Month/Year " + date_greatest_increase + " " + format_greatest_increase)
    analysis.write("Greatest Decrease in Profits: " + "Month/Year " + date_greatest_decrease + " " + format_greatest_decrease)