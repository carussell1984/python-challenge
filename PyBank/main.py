#first step is to read CVS in order to work with the file
#import os will allow us to creat file paths across operating systems
import os

#import module for reading CVS files
import csv

#set the path to open the file
csvpath = os.path.join('budget_data.csv')

#generate count_month for counting rows since each row is a month
#generae the total to sum all of the profits and losses during the loop
#generate profit_loses array to perform another loop to get the difference between months
#generate date array to use in the second loop
count_month = 0
total  = 0 
profit_loses = []
date = []


#read CSV module looping throug rows to perform the following actions:
    # i. count in the rows (number of months)
    # ii. summing the total of profits/loses
    # iii. formating the total from aggregate sum for profit loses
    # iV. creating two arrays - date array & profit/loses for the second loop
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    for row in csvreader: 
        #print (row)
        count_month = count_month + 1
        total += float(row[1])
        total_format = '${:,.2f}'.format(total)
        profit_loses.append(int(row[1]))
        date.append(row[0])
        
      
#initalize:
    # i. delta_change, or the difference between to months
    # ii. greatest_increase & greatest_decrease 
delta_change = 0
greatest_increase = (profit_loses[1] - profit_loses[0])
greatest_decrease = (profit_loses[1] - profit_loses[0])

# loop through the list/array of profit/loses to find all the changes, and then determine which changes are the greatest increase and the greatest decrease
for i in range(0,len(profit_loses)):
    if i >= 1:
        delta_change += (profit_loses[i] - profit_loses[i-1])
    if greatest_increase <= (profit_loses[i] - profit_loses[i-1]): 
        greatest_increase = (profit_loses[i] - profit_loses[i-1])
        date_greatest_increase = date[i]
    if greatest_decrease >= (profit_loses[i] - profit_loses[i-1]):
        greatest_decrease = (profit_loses[i] - profit_loses[i-1])
        date_greatest_decrease = date[i]

#the average change is a sum of all the deltas between the months divided by the number of times the operation occured in the above for loop
average_change = delta_change/(count_month-1)

#format to two decimals
round_average_change = round(average_change, 2)

#format to US currency
total_average = '${:,.2f}'.format(round_average_change)

#format to US currency
format_greatest_increase = '${:,.2f}'.format(greatest_increase)

#format to US currency
format_greatest_decrease = '${:,.2f}'.format(greatest_decrease)



#set the path for the results to print out to
results = os.path.join("pybankanalysis.txt")


# this action will create a file with there is not one already open, and will write the following items
with open(results,"w+") as analysis:
    analysis.write("\n")
    analysis.write("Financial Analysis\n")
    analysis.write("-----------------------\n")
    analysis.write("Total Months: " + str(count_month) + "\n")
    analysis.write("Total: " + str(total_format) + "\n")
    analysis.write("Average Change: " + str(total_average) + "\n")
    analysis.write("Greatest Increase in Profits: " + "Month/Year-" + date_greatest_increase + " " + format_greatest_increase + "\n")
    analysis.write("Greatest Decrease in Profits: " + "Month/Year-" + date_greatest_decrease + " " + format_greatest_decrease + "\n")

#open what was been written above & reads the txt file
readanalysis = open(results, "r")
read = readanalysis.readlines()
for lines in read:
    print(lines)
