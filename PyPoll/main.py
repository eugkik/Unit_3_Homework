import os
import csv

#source_data = os.path.join('Resources', 'Book1.csv')
source_data = os.path.join('Resources', 'election_data.csv')

#list to contain only candidate names from every row in csv file
all_candidates = []

#list to contain unique candidate names
unique_candidates = []

# list to contain unique candidate names and their total vote counts
totals = []

# read csv file and skip header row
with open(source_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
  
# candidate name into poll_data list, put unique names into unique_candidate list  
    for row in csvreader:
        all_candidates.append(row[2])
        if (row[2]) not in unique_candidates:
            unique_candidates.append(row[2])


for names in unique_candidates:
    counts = all_candidates.count(names)
    totals.append([counts,names])    

total_votes = len(all_candidates)
totals.sort(reverse=True)
print(totals)
print('Election Results')
print('---------------------------------')
print(f'Total Votes: {total_votes}')
print('---------------------------------')
for x in range(len(totals)):
   percent_votes = totals[x][0]/total_votes*100
   print(f"{totals[x][1]}: {format(percent_votes, '.3f')}% ({totals[x][0]})")
   #print(f'{totals[x][1]}: {totals[x][0]/total_votes*100}% ({totals[x][0]})')

print('---------------------------------')
print(f'Winner: {totals[0][1]}')
print('---------------------------------')
