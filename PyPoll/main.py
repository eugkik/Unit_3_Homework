import os
import csv

#define source path for csv file
source_data = os.path.join('Resources', 'election_data.csv')

#list to contain candidate names from every row in csv file
all_candidates = []

#list to contain unique candidate names
unique_candidates = []

#list to contain unique candidate names and their total vote counts
candidate_votes = []

#read csv file and skip header row
with open(source_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)

#loop through all rows and append candidate name into all_candidates list
#if candidate name is not in unique_candidate list, append into list
    for row in csvreader:
        all_candidates.append(row[2])
        if (row[2]) not in unique_candidates:
            unique_candidates.append(row[2])

#loop through each name in unique_candidates list
#count name occurrences in all_candidates list to determine total votes for name
#append list of vote count and name into candidate_votes list
for names in unique_candidates:
    counts = all_candidates.count(names)
    candidate_votes.append([counts,names])    

#find total votes cast in election from length of all_candidates list
total_votes = len(all_candidates)

#reverse sort candidate_votes list to order candidates from highest to lowest votes
candidate_votes.sort(reverse=True)

#print output to terminal
print('Election Results')
print('---------------------------------')
print(f'Total Votes: {total_votes}')
print('---------------------------------')

#loop through number of unique candidates
#calculate percent of votes received for each unique candidate
#print formatted output to terminal
for x in range(len(candidate_votes)):
   percent_votes = candidate_votes[x][0]/total_votes*100
   print(f"{candidate_votes[x][1]}: {format(percent_votes, '.3f')}% ({candidate_votes[x][0]})")

#print element 0 from sorted candidate_votes list as winner to terminal
print('---------------------------------')
print(f'Winner: {candidate_votes[0][1]}')
print('---------------------------------')

#write output to text file
output_path = os.path.join('Analysis', 'PyPoll_Results.txt')
with open(output_path, 'w') as text_out:
    print('Election Results', file = text_out)
    print('---------------------------------', file = text_out)
    print(f'Total Votes: {total_votes}', file = text_out)
    print('---------------------------------', file = text_out)
    for x in range(len(candidate_votes)):
        percent_votes = candidate_votes[x][0]/total_votes*100
        print(f"{candidate_votes[x][1]}: {format(percent_votes, '.3f')}% ({candidate_votes[x][0]})", file = text_out)
    print('---------------------------------', file = text_out)
    print(f'Winner: {candidate_votes[0][1]}', file = text_out)
    print('---------------------------------', file = text_out)