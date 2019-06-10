#import programs
import os
import csv

#set csvpath to open the csvfile
csvpath = os.path.join("election_data.csv")

#set the counts for all the candiates to 0, and as it scans through the row and sees the deligate it will count
#alternatively I think a diction could be created as it scans through or the dict read could be used
#I'm going to work on these alternative code for practice, but submit this since it works!
khan = 0
correy = 0
li = 0
otooley = 0
vote = 0


# open the file, printing for confirmation that the correct file is opening, and skipping the first line during the loop
# as stated above, each row is a vote cast so the vote count tallying up on each rown
# similarly for each of the candidates, there is a vote count if there name is recognized
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header=next(csvreader)
    

   

    for row in csvreader:
        vote = vote + 1 
        if row[2] == "Khan":
            khan = khan + 1
        elif row[2] == "Correy":
            correy = correy + 1
        elif row[2] == "Li":
            li = li + 1
        elif row[2] == "O'Tooley":
            otooley = otooley + 1


#calculations & formating. I definetly think creating a dictionary as one loops through the rows would down size the rows and the codelines
#also, I can not get in the print out for three decimal places. Need to continue working on this
percent_khan= (khan/vote) * 100
format_per_khan = round(percent_khan, 3)
format2_per_khan = "{0}%".format(format_per_khan)


percent_correy= (correy/vote) * 100
format_per_correy = round(percent_correy, 3)
format2_per_correy = "{0}%".format(format_per_correy)

percent_li= (li/vote) * 100
format_per_li = round(percent_li, 3)
format2_per_li= "{0}%".format(format_per_li)

percent_otooley= (otooley/vote) * 100
format_per_otooley = round(percent_li, 3)
format2_per_otooley= "{0}%".format(format_per_otooley)

#Finally, a bit of logic to determine the winner. Khan is first and is the winner, but I rearranged order to test this 
winner = "winner"
x = 0

if khan > x: 
    winner = "Khan"
if correy > khan:
    winner = "Correy"
if li > correy:
    winner = "Li"
if otooley > li:
    winner = "O'tooley" 

#create path for the test file
results = os.path.join("pypollanalysis.txt")

#open and write to txt, and then read and print what has been written
with open(results, "w+") as analysis:
    analysis.writelines("Election Results\n")
    analysis.writelines("------------------------------------------------\n")
    analysis.writelines("Total Votes: " + str(vote) + "\n")
    analysis.writelines("------------------------------------------------\n")
    analysis.writelines("Khan: " + format2_per_khan + " (" + str(khan) + ")\n")
    analysis.writelines("Correy: " + format2_per_correy + " (" + str(correy) +")\n")
    analysis.writelines("Li: " + format2_per_li + " (" + str(li) +")\n")
    analysis.writelines("O'Tooley: " + format2_per_otooley + " (" + str(otooley) +")\n")
    analysis.writelines("------------------------------------------------\n")
    analysis.writelines("The Winner of the election is : " + winner + "\n")
    analysis.writelines("------------------------------------------------\n")

readanalysis = open(results, "r")

read = readanalysis.readlines()

for lines in read:
    print(lines)



