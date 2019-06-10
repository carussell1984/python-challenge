#import dependancies to use during the program to read file and work with csv file
import os
import csv

#set the csvpathreleative to script
csvpath = os.path.join("election_data.csv")

#create a named empty dictionary where by the candidate names and the counts will be cast into
poll_results = {}
total_votes = 0

#open the the file and set a loop to read down the columns, adding the candidate to the 
#and counting the value of the candidate
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate not in poll_results:
            poll_results[candidate] = 1
        else:
            poll_results[candidate] += 1
    

#find the winner by using the max and then calling the key with the get function
winner = max(poll_results, key=poll_results.get)



#print the results to the screen
print("-------------------------------------------\n")
print("Election Results\n")
print("-------------------------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-------------------------------------------\n")
for key, value in poll_results.items():
    percentage_str = str(round((value/total_votes)*100,3)) + "%"
    print(f"{key}: {percentage_str}  ({value})\n" )
print("-------------------------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------------------------\n")

#set the file to write to a text file
pollresults = os.path.join("pypollanalysis2.txt")

with open(pollresults, "w+") as pollresults:
    pollresults.writelines("-------------------------------------------\n")
    pollresults.writelines("Election Results\n")
    pollresults.writelines("-------------------------------------------\n")
    pollresults.writelines(f"Total Votes: {total_votes}\n")
    pollresults.writelines("-------------------------------------------\n")
    for key, value in poll_results.items():
        percentage_str = str(round((value/total_votes)*100,3)) + "%"
        pollresults.writelines(f"{key}: {percentage_str}  ({value})\n" )
    pollresults.writelines("-------------------------------------------\n")
    pollresults.writelines(f"Winner: {winner}\n")
    pollresults.writelines("-------------------------------------------\n")

