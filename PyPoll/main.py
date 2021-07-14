import os
import csv

#source_data = os.path.join('Resources', 'Book1.csv')
source_data = os.path.join('Resources', 'election_data.csv')

#list to contain only candidate names from every row in csv file
all_candidates = []

#list to contain unique candidate names
unique_candidates = []

#list to contain unique candidate names and their total vote counts
totals = []

#read csv file and skip header row
with open(source_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
  
#loop through all rows and append candidate name into all_candidates list
#if candidate name is not unique_candidate list, append into list
    for row in csvreader:
        all_candidates.append(row[2])
        if (row[2]) not in unique_candidates:
            unique_candidates.append(row[2])

#loop through each name in unique_candidates list
#count name occurances in all_candidates list to determine total votes for name
#append vote count and name into totals list
for names in unique_candidates:
    counts = all_candidates.count(names)
    totals.append([counts,names])    

#find total votes cast from lenght of all_candidates list
total_votes = len(all_candidates)

#reverse sort totals list to order candidates from highest to lowest votes
totals.sort(reverse=True)

#print output to terminal
print(totals)
print('Election Results')
print('---------------------------------')
print(f'Total Votes: {total_votes}')
print('---------------------------------')

#loop through number of unique candidates
#for each candidate, calculate percent of votes received
#print formatted output to terminal
for x in range(len(totals)):
   percent_votes = totals[x][0]/total_votes*100
   print(f"{totals[x][1]}: {format(percent_votes, '.3f')}% ({totals[x][0]})")
 
#print element 0 from sorted totals list as winner to terminal
print('---------------------------------')
print(f'Winner: {totals[0][1]}')
print('---------------------------------')

#write output to text file
output_path = os.path.join('Analysis', 'PyPoll_Results.txt')
with open(output_path, 'w') as text_out:
    print("Financial Analysis", file = text_out)
    print(totals, file = text_out)
    print('Election Results', file = text_out)
    print('---------------------------------', file = text_out)
    print(f'Total Votes: {total_votes}', file = text_out)
    print('---------------------------------', file = text_out)
    for x in range(len(totals)):
        percent_votes = totals[x][0]/total_votes*100
        print(f"{totals[x][1]}: {format(percent_votes, '.3f')}% ({totals[x][0]})", file = text_out)
    print('---------------------------------', file = text_out)
    print(f'Winner: {totals[0][1]}', file = text_out)
    print('---------------------------------', file = text_out)