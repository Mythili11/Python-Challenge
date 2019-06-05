import os
import csv

# Import CSV here
file = os.path.join('..', 'Resources', 'budget_data.csv')

   
# Lists to store data
dates = []
money = []
change =[]
previous = 0

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    for row in csvreader:
        dates.append(row[0])
        money.append(row[1])
        
        diff = int(row[1]) - int(previous)
        previous = row[1]
        change.append(diff)

zipped = zip(dates, change)
zipped_lst = list(zipped)
change.remove(change[0])
zipped_lst.remove(zipped_lst[0])
  
total_months = len(dates)
total = sum(map(int, money))
average_change = sum(change) / len(change)
increase = max(change)
decrease = min(change)

month_dec = 0
month_inc = 0

for row in zipped_lst:
    if row[1] == increase:
        month_inc = row[0]
    if row[1] == decrease:
        month_dec = row[0]

print(f'Financial Analysis')
print(f'___________________________')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {month_inc} ({increase})')
print(f'Greatest Decrease in Profits: {month_dec} ({decrease})')
i = 0

with open("Output.txt","w") as output:
    output.write('Financial Analysis')
    output.write("\n")
    output.write("___________________________\n")
    output.write("\n")
    output.write(f'Total Months: {total_months}')
    output.write("\n")
    output.write(f'Total: ${total}')
    output.write("\n")
    output.write(f'Average Change: ${average_change:.2f}')
    output.write("\n")
    output.write(f'Greatest Increase in Profits: {month_inc} ({increase})')
    output.write("\n")
    output.write(f'Greatest Decrease in Profits: {month_dec} ({decrease})')
    output.write("\n")