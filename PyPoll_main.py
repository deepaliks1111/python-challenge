# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:47:57 2018
@author: Deepali
Subject: PY Poll analysis
"""

#importing libraries
import csv

## Declaring global variables
# Constants
verbose = True
writeOutputToFile = True
inputFile  = "election_data.csv"
outputFile = "Poll_analysis.txt"
# Data variables
analysis = [] # analysis as list
data_as_list = []
tot_votes = 0 # The total number of votes cast
candidates = []
poll_results = [] # A complete list of candidates who received votes
winner = 'None'

#Open cvs file and read
with open(inputFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ignoreHeader = True
    tot_votes = 0
    for row in csv_reader:
        if ignoreHeader :
            ignoreHeader = False
            continue
        data_as_list.append([row[0],row[1],row[2]]) 
        tot_votes += 1
    if verbose: print('>>> Completed CSV File Reading')

## Analyze data
# Get unique candidates
all_candidates = [row[2] for row in data_as_list]
for x in all_candidates:
    if x not in candidates:
        candidates.append(x)
'''
# Alternate way to Get unique candidates
tempset = set(all_candidates)
candidates = list(tempset)
'''
if verbose: print('>>> unique candidates identified', candidates)

# Count votes
poll_results = [0] * len(candidates)
for row in data_as_list :
    candidate_name = row [2]
    candidate_number = candidates.index(candidate_name)
    vote_cnt = poll_results [candidate_number] + 1
    poll_results [candidate_number] = vote_cnt 

# Identify winner
#winner = candidates[0]
vote_cnt = -99999
for i in range (len(candidates)):
    if (int(poll_results[i]) > vote_cnt ):
        winner = candidates[i]
        vote_cnt = poll_results[i]

#Generate analysis report
analysis.append ('Election Results')
analysis.append ('-------------------------')
analysis.append ('Total Votes: ' + str(tot_votes))
analysis.append ('-------------------------')
for i in range (len(candidates)):
    percent_won = (poll_results[i] / tot_votes) * 100
    vote_count = poll_results[i]
    analysis.append (candidates[i] + ': ' 
                     + str(percent_won) + '% (' 
                     + str(vote_count) + ')')
analysis.append ('-------------------------')
analysis.append ('Winner: ' + str(winner))
analysis.append ('-------------------------')

#print analysis
for line in analysis:
    print (line)
if verbose: print('>>> Completed printing analysis')

#Write analysis to file
if (writeOutputToFile) :
    file = open(outputFile,"w")
    for line in analysis:
        file.writelines (str(line) + '\n')
    file.close()
if verbose: print('>>> Completed writing analysis to file')
    
 
