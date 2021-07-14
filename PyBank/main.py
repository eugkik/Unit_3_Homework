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
    greatest_increase = 0
    greatest_decrease = 0

#initialize variable for
    m_ave = 0
    csv_first = next(csvreader)
    last_month = int(csv_first[1])
    total_amount = last_month

    for row in csvreader:
        raw_data.append(row)
        total_amount = total_amount + int(row[1])

        average = int(row[1]) - last_month
        m_ave = m_ave + average

        if average > greatest_increase:
            greatest_increase = average
            increase_month = row[0]
        elif average <  greatest_decrease:
            greatest_decrease = average
            decrease_month = row[0]
        last_month = int(row[1])

total_months = int(len(raw_data))

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months + 1}")
print(f"Total: {total_amount}")
print(f"Average Change: {m_ave/total_months}")
print(f"Greatest Increase in Profits: {increase_month} ({greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} ({greatest_decrease})")

output_path = os.path.join('Analysis', 'PyBank_Results.txt')
with open(output_path, 'w') as text_out:
    print("Financial Analysis", file = text_out)
    print("--------------------------", file = text_out)
    print(f"Total Months: {total_months + 1}", file = text_out)
    print(f"Total: {total_amount}", file = text_out)
    print(f"Average Change: {m_ave/total_months}", file = text_out)
    print(f"Greatest Increase in Profits: {increase_month} ({greatest_increase})", file = text_out)
    print(f"Greatest Decrease in Profits: {decrease_month} ({greatest_decrease})", file = text_out)