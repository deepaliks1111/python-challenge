# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:47:57 2018
@author: Deepali
Subject: PY Bank analysis
"""

#importing libraries
import csv

## Declaring global variables
# Constants
verbose = False
writeOutputToFile = True
inputFile  = "budget_data.csv"
outputFile = "PyBank_analysis.txt"
# Data variables
analysis = [] # analysis as list
data_as_list = []

#Analysis variables
tot_months = 0 # The total number of months included in the dataset
tot_profit = 0 # The total net amount of "Profit/Losses" over the entire period
avg_change = 0 # The average change in "Profit/Losses" between months over the entire period
max_profit = 0 # The greatest increase in profits (date and amount) over the entire period
max_profit_date = 0
min_losses = 0 # The greatest decrease in losses (date and amount) over the entire period
min_losses_date = 0

#Open cvs file and read
with open(inputFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ignoreHeader = True
    for row in csv_reader:
        if ignoreHeader :
            ignoreHeader = False
            continue
        data_as_list.append([row[0],row[1],0])  
    if verbose: print('>>> Completed CSV File Reading')

# Analyze data
previous_month_profit = data_as_list[0][1]
tot_change_in_profit = 0
max_profit = -9999999
min_losses = +9999999
    
for row in data_as_list:
    tot_months += 1 # same as tot_months = tot_months + 1
    tot_profit += int(row [1])
    #calculating change in profit
    change = int(row[1]) - int(previous_month_profit)
    row[2] = change
    tot_change_in_profit += change
    previous_month_profit = row[1]

    #select row with max profit
    if (max_profit < int(row[1]) ):
        max_profit = int(row[1])
        max_profit_date = row[0]

    #select row with min losses
    if (min_losses > int(row[1]) ):
        min_losses = int(row[1])
        min_losses_date = row[0]

avg_change = tot_change_in_profit / tot_months 
         
    
#Generate analysis report
analysis.append ('Financial Analysis')
analysis.append ('----------------------------')
analysis.append ('Total Months: ' + str(tot_months))
analysis.append ('Total: $' + str(tot_profit))
analysis.append ('Average  Change: $' + str(avg_change))
analysis.append ('Greatest Increase in Profits: ' 
                 + str(max_profit_date) + ' ($'
                 + str(max_profit)  +')')
analysis.append ('Greatest Decrease in Profits: '
                 + str(min_losses) + ' ($'
                 + str(min_losses_date) +')')
    
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
    
 
