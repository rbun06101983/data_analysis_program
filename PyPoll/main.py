#Dependencies
import os
import csv

#creating object out of csv file
election_data=os.path.join('Resources', "election_data.csv")

candidates=[]
voter_id=[]
num_votes=[]
per_votes=[]
total_votes=0

#opening and reading the csv file
with open(election_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

    for row in csvreader:
        #Add to voter count
        total_votes +=1

        '''
        If the candidates is not on our list, add his/her name to our list, along with 
        a vote in his/her name.
        If he/she is already on our list, we will simply add a vote in his/her
        name 
        '''
        if row[2] not in candidates:
            candidates.append(row[2])
            index=candidates.index(row[2])
            num_votes.append(1)
        else:
            index=candidates.index(row[2])
            num_votes[index] +=1
    
    #Add to % vote list
    for votes in num_votes:
        percentage=(votes/total_votes)*100
        percentage= '%.3f%%'% percentage
        per_votes.append(percentage)
    
    #Find the winner
    winner=max(num_votes)
    index=num_votes.index(winner)
    winning_candidate=candidates[index]

#Results
print('Election Results')
print('------------------')
print(f'Total Votes:{str(total_votes)}')
print('------------------')
for i in range(len(candidates)):
    print(f'{candidates[i]}: {str(per_votes[i])}({str(num_votes[i])})')
print('------------------')
print(f'Winner: {winning_candidate}')
print('------------------')

#Exporting to text file
output=open('output.txt', 'w')
line1='Election Results'
line2='------------------'
line3=(f'Total Votes:{str(total_votes)}')
line4='------------------'
output.write('{}\n{}\n{}\n{}n'.format(line1,line2,line3,line4))
for i in range(len(candidates)):
    line=str(f'{candidates[i]}: {str(per_votes[i])}({str(num_votes[i])})')
    output.write('{}\n'.format(line))
line5='------------------'
line6=str(f'Winner: {winning_candidate}')
line7='------------------'
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))

