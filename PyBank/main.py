#Dependencies
import os
import csv

#creating object out of csv file
budget_data=os.path.join('Resources' ,"budget_data.csv")

total_months=0
total_pl=0
value=0
change=0
dates=[]
profits=[]

#opening and reading the csv file
with open(budget_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #Reading the header row
    csv_header=next(csvreader)

    #Readiing the first row
    first_row=next(csvreader)
    total_months +=1
    total_pl += int(first_row[1])
    value=int(first_row[1])

    #Going throguh each row of data
    for row in csvreader:
        #Date tracking
        dates.append(row[0])

        #Cacluate change then adding to change list
        change = int(row[1])-value
        profits.append(change)
        value=int(row[1])

        #total number of months
        total_months +=1

        #total net "Profit/Losses"
        total_pl=total_pl + int(row[1])

    #greatest profit increase
    greatest_increase=max(profits)
    greatest_index=profits.index(greatest_increase)
    greatest_date=dates[greatest_index]

    #greates profit decrease
    greatest_decrease=min(profits)
    lowest_index=profits.index(greatest_decrease)
    lowest_date=dates[lowest_index]

    #Average Change
    avg_change=sum(profits)/len(profits)

#Displaying information
print('Financial Analysis')
print('-------------------------')
print(f'Total Months:{str(total_months)}')
print(f'Total:${str(total_pl)}')
print(f'Average Change:${str(round(avg_change,2))}')
print(f'Greatest Increase in Profits:{greatest_date} (${str(greatest_increase)})')
print(f'Greatest Decrease in Profits:{lowest_date} (${str(greatest_decrease)})')

#Exporting to text file
output= open('output.txt', 'w')

line1='Financial Analysis'
line2='-------------------------'
line3=str(f'Total Months:{str(total_months)}')
line4=str(f'Total:${str(total_pl)}')
line5=str(f'Average Change:${str(round(avg_change,2))}')
line6=str(f'Greatest Increase in Profits:{greatest_date} (${str(greatest_increase)})')
line7=str(f'Greatest Decrease in Profits:{lowest_date} (${str(greatest_decrease)})')
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
