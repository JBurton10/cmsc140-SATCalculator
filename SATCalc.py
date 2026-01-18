'''
James Burton
CMSC 140
What state had the highest average sat score between 2005 and 2015?
'''
#imports csv reader
import csv
#defines function to extract a column of data from any csv file
def extract_column(csv_file, column_name):
    column_data = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if column_name in row:
                column_data.append(row[column_name])
    return column_data

#extracts the relevant columns to store in lists
total_math = extract_column('school_scores.csv', 'Total.Math')
total_reading = extract_column('school_scores.csv', 'Total.Verbal')
states = extract_column('school_scores.csv', 'State.Name')
year = extract_column('school_scores.csv', 'Year')


    
#establish two dictionaries to later calculate the average per state over the ten year span
state_totals = {}
state_counts = {}

#runs through each value in the column "states" and updates the key value to have the correct total
for i in range(len(states)):
    state = states[i]
    total_score = int(total_math[i]) + int(total_reading[i])
    
    # This updates total score for the state
    if state in state_totals:
        state_totals[state] += total_score
        state_counts[state] += 1
    else:
        state_totals[state] = total_score
        state_counts[state] = 1


#initializing two variable to keep track of the highest average sat score
highest_average_score = 1
highest_average_state = None

# Calculate and print average total scores per state
for state in state_totals:
    total_score = state_totals[state] #sets the total score per state equal to the sum of all the average sat scores
    count = state_counts[state]#sets the number of times the state is repeated
    average_score = total_score / count#finds the average sat score per state across the 10 year span
    print("State:", state)
    print("Average SAT Score:", average_score)
    print()

    #keeps track of the highest average score 
    if average_score > highest_average_score:
        highest_average_score = average_score
        highest_average_state = state

print ("***************************************************")        
print("Highest Average SAT Score:", highest_average_state, highest_average_score)
print ("***************************************************")        

