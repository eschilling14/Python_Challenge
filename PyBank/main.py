import os
import csv

total_months = 0
month_change = []
net_change_list = []
net_increase = ["", 0]
net_decrease = ["", 999999999999]
net_total = 0

budget_data = os.path.join(".." , "PyBank", "budget_data.csv")
outputfile = os.path.join("pybank_homework.txt")
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    
    first_row=next(csvreader)
    total_months = total_months + 1
    net_total = net_total + int(first_row[1])
    prev_net = int(first_row[1])
    

    for row in csvreader:

        total_months = total_months + 1
        net_total = net_total + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_change = month_change + [row[0]]

    if net_change > net_increase[1]:
        net_increase[0] = row[0]
        net_increase[1] = net_change

    if net_change < net_decrease[1]:
        net_decrease[0]=row[0]
        net_decrease[1]=net_change

    net_monthly_change= sum(net_change_list)/len(net_change_list)

final = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${net_change:.2f}\n"
    f"Greatest Increase in Profits: {net_increase[0]} (${net_increase[1]})\n"
    f"Greatest Decrease in Profits: {net_decrease[0]} (${net_decrease[1]})\n")

print(final)

with open(outputfile, "w") as text_file:
    text_file.write(final)



