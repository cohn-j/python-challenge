#Import modules for path creation and reading of the initial .CSV file.
import os
import csv

#String that is the .CSV path.
budget_csv = os.path.join('Resources','budget_data.csv')

#Variable to store the total # of months once the file has been read.
num_months = 0
#variable to store the total # profit/loss once the file has been read.
total_profit = 0

#Variables to calculate the difference between the current month and prior month.
profit_month1 = 0
profit_month2 = 0
monthly_profit = 0.00
#variable to track the greatest month-over-month profit increase and the corresponding month it took place.
Greatest_Inc_Amt = 0
Greatest_Inc_Month = ""
#Variable to track the greatest month-over-motnh profit decrease and the corresponding month it took place.
Greatest_Dec_Amt = 0
Greatest_Dec_Month = ""

#code to open the .CSV file and move past the header row.
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:
        #Each iteration of the for loop adds one to the overall month calculation. Total # of rows excluding the header is the 
        # # of months of data the file contains.
        num_months += 1
        # Each iteration of the for loop will add the 2nd item in the list (profit/loss) to the variable to 
        # obtain the overall profit/loss to date
        total_profit += int(row[1])
        #If statement to track the month over month profit/loss change and then 
        # ultimately calculate the average within the summary list.
        if num_months == 1:
            profit_month1 = int(row[1])
            profit_month2 = 0
            Greatest_Inc_Amt = profit_month1 - profit_month2
            Greatest_Dec_Amt = profit_month1 - profit_month2
            Greatest_Inc_Month = row[0]
            Greatest_Dec_Month = row[0]
        elif num_months > 1:
            profit_month2 = profit_month1
            profit_month1 = int(row[1])
            monthly_profit = monthly_profit + profit_month1 - profit_month2
            #the following if statements track the greatest increases and decreases of the month-over-month changes. The variables will be overwritten if the current month's value minus the value of the prior  is > or < depending on which stat is being reviewed.
            if (profit_month1 - profit_month2) > Greatest_Inc_Amt:
                Greatest_Inc_Amt = profit_month1 - profit_month2
                Greatest_Inc_Month = row[0]    
            else:
                Greatest_Inc_Amt = Greatest_Inc_Amt
                Greatest_Inc_Month = Greatest_Inc_Month
            if(profit_month1 - profit_month2) < Greatest_Dec_Amt:
                Greatest_Dec_Amt = profit_month1 - profit_month2
                Greatest_Dec_Month = row[0]
            else:
                Greatest_Dec_Amt = Greatest_Dec_Amt
                Greatest_Dec_Month = Greatest_Dec_Month        
#adding the verbiage and corresponding data to the summary list variable:
summary = ["Total months: " + str(num_months),
    "Total: $" + str(total_profit),
    "Average change: $"+str(round(float(monthly_profit / int(num_months-1)),2)),
    "Greatest Increase in Profits: " + Greatest_Inc_Month + " ($" + str(Greatest_Inc_Amt) + ")",
    "Greatest Decrease in Profits: " + Greatest_Dec_Month + " ($" + str(Greatest_Dec_Amt) + ")",]
#prints the analysis to the terminal:
print("Financial Analysis:")
print("-------------------")
for row in summary:
    print(row)

#writes the analysis to a .txt file. The "\n" is to drop each result to a new line to make the results more visually appealing.
analysis_txt = os.path.join('Analysis','analysis.txt')
with open(analysis_txt,'w') as txtfile:

    txtfile.write("Financial Analysis: \n")
    txtfile.write("------------------- \n")
    for row in summary:
        txtfile.write(row + "\n")