# Import pathlib and csv livbrary
import pandas as pd
df = pd.read_csv ("C:\\Users\\hecto\\OneDrive\\Desktop\\Rutgers\\Class-Work\\02-Homework\\02-Python\\Instructions\\PyBank\\Resources\\budget_data.csv")
print (df)


# set file path
budget_data_csvpath = ("C:\\Users\\hecto\\OneDrive\\Desktop\\Rutgers\\Class-Work\\02-Homework\\02-Python\\Instructions\\PyBank\\Resources\\budget_data.csv")

#set output text file
text_path = "output.txt"

# data variables
total_months= 0
total_revenue = 0
previous_revenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]

# Read budget_data.csv file
import csv
with open("C:\\Users\\hecto\\OneDrive\\Desktop\\Rutgers\\Class-Work\\02-Homework\\02-Python\\Instructions\\PyBank\\Resources\\budget_data.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)

# loop for total months
for row in csvreader:

    #Monthly totals
    total_months = total_months + 1
    total_revenue = total_revenue + int(row["Profit/Losses"])

# total change in revenue over entire period
revenue_change = int(row["Profit/Losses"]) - previous_revenue
previous_revenue = int(row["Profit/Losses"])
month_of_change = month_of_change + [row["Date"]]

# Calc average change in revenue between months over period
revenue_change = int(row["Profit/Losses"])- previous_revenue
previous_revenue = int (row["Profit/Losses"])
revenue_change_list = revenue_change_list + [revenue_change]
month_of_change = month_of_change + [row["Date"]]

# greatest increase 
if (revenue_change > greatest_increase[1]):
    greatest_increase[1] = revenue_change
    greatest_increase[0] = row["Date"]

# greatest decrease
if (revenue_change < greatest_decrease[1]):
    greatest_decrease[0] = row["Date"]
    greatest_increase[1] = revenue_change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


#print results
output = (
        f"Total Months:  {total_months}\n")
(f"Total Revenue: {total_revenue}\n"
f"Average Revenue Change: ${revenue_avg}\n"
f"Greatest increase in Revenue: {greatest_increase[0]} ${greatest_increase[1]}\n"
f"Greatest decrease in Revenue: {greatest_decrease[0]} ${greatest_decrease[1]}\n")

print ("Financial Analysis")
print ("total_months: {line_num}")
print ("total: {profitloss_sum}")
print("Average Change: ${average_change_profitloss}")
print("Greatest Increase in Profits: ${Date} on {Profit/Losses}")
print("Greatest Decrease in Profits: ${Date} on {Profit/Losses}")



#text to path
with open(text_path, "w") as txt_file:
    txt_file.write(output)
