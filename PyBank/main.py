import os
import csv

#define source path for csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#list to contain 
raw_data = []

#read csv file and skip header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#initialize variables for greatest increase and decrease in profits
    greatest_increase_amount = 0
    greatest_decrease_amount = 0

#initialize variable for total monthly profit/loss
    monthly_total = 0

#read first row of profit data
#set initial values for calculating monthly average change
    csv_first = next(csvreader)
    last_month = int(csv_first[1])

#initialize variable for cumulative profit totals
    total_amount = int(csv_first[1])

#loop through all remaining rows and append date and profit data into list
#keep running total of profits
    for row in csvreader:
        raw_data.append(row)
        total_amount = total_amount + int(row[1])

#calculate monthly profit/loss
        monthly_change = int(row[1]) - last_month

#calculate cumulative total monthly profit/loss
        monthly_total = monthly_total + monthly_change

#compare current month's profit with greatest profit variable
#record current month and amount if greater
        if monthly_change > greatest_increase_amount:
            greatest_increase_amount = monthly_change
            greatest_increase_month = row[0]

#compare current month's loss with greates loss variable
#record current month and amount if less
        elif monthly_change <  greatest_decrease_amount:
            greatest_decrease_amount = monthly_change
            decrease_month = row[0]

#set variable for next iteration
        last_month = int(row[1])

#find total months from length of list
total_months = int(len(raw_data))

#print output to terminal
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months + 1}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${round(monthly_total/total_months,2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease_amount})")

#print output to text file
output_path = os.path.join('Analysis', 'PyBank_Results.txt')
with open(output_path, 'w') as text_out:
    print("Financial Analysis", file = text_out)
    print("--------------------------", file = text_out)
    print(f"Total Months: {total_months + 1}", file = text_out)
    print(f"Total: ${total_amount}", file = text_out)
    print(f"Average Change: ${round(monthly_total/total_months,2)}", file = text_out)
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})", file = text_out)
    print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease_amount})", file = text_out)