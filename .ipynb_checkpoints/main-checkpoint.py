# Open budget_data.csv and populate a dictionary of {Date : Profilt and Loss} as the Key : Value pairs
import csv
with open('budget_data.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    Profit_Loss_Data = {rows[0]:rows[1] for rows in reader}
# Delete the first entry in the dictionary as this is the column headers
del Profit_Loss_Data ['Date']
# Initialize metric variables
Total_Months = 0
Total = 0
# For loop to calcuate total Net Profit and Loss and Total Months
for date, Profit_Loss in Profit_Loss_Data.items():
    print(f"Date: {date} | Profit/Loss: {Profit_Loss}")
    # calc number of months
    Total_Months += 1
    # calc net total
    Total += int(Profit_Loss)
#Create list from values in dictionary with monthly accruals from Profit Loss Data
Accruals =list(Profit_Loss_Data.values())
for i in range(0, len(Accruals)):
    Accruals[i] = int(Accruals[i])
#Create list of differences between items in Accruals list
Changes_in_Profit_Loss = [x - Accruals[i - 1] for i, x in enumerate(Accruals)][1:]
#Calcualte total change in Profit and Loss by summing the items in the Changes_in_Profit_Loss list.
Total_Changes_in_Profit_Loss = sum(Changes_in_Profit_Loss)
# Calcuate average change in profit and loss per month
Avaerage_Change_in_Profit_Loss = Total_Changes_in_Profit_Loss/len(Changes_in_Profit_Loss)
#Calautate the both the greatest increase and decrease in profits.
Greatest_Increase_in_Profits = max(Changes_in_Profit_Loss)
Greatest_Decrease_in_Profits = min(Changes_in_Profit_Loss)
#Determine the index in list where the greatest increase in profits occured. We need to add one here because the Changes_in_Profit_Loss list is one less than the Accruals list.
Greatest_Increase_in_Profits_Index = Changes_in_Profit_Loss .index(Greatest_Increase_in_Profits) +1
#Find the corresponding item in the Accruals list to the index of the Greatest_Increase_in_Profits_Month list. This will give us the Profit and Loss value with the largest increase in profit. 
Greatest_Increase_Month_Lookup = Accruals[Greatest_Increase_in_Profits_Index]
for key, value in Profit_Loss_Data.items():
    if value == str(Greatest_Increase_Month_Lookup):
        print(key)
        Greatest_Increase_in_Profits_Month = key
#Determine the index in list where the greatest decrease in profits occured. We need to add one here because the Changes_in_Profit_Loss list is one less than the Accruals list.
Greatest_Decrease_in_Profits_Index = Changes_in_Profit_Loss .index(Greatest_Decrease_in_Profits) +1
#Find the corresponding item in the Accruals list to the index of the Greatest_Decrease_in_Profits_Month list. This will give us the Profit and Loss value with the largest decrease in profit. 
Greatest_Decrease_Month_Lookup = Accruals[Greatest_Decrease_in_Profits_Index]
for key, value in Profit_Loss_Data.items():
    if value == str(Greatest_Decrease_Month_Lookup):
        print(key)
        Greatest_Decrease_in_Profits_Month = key
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change ${Avaerage_Change_in_Profit_Loss:.2f}")
print(f"Greatest Increase in Profits: {Greatest_Increase_in_Profits_Month} (${Greatest_Increase_in_Profits})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_in_Profits_Month} (${Greatest_Decrease_in_Profits})")

from pathlib import Path
output_path = Path("output.txt")

# Open the output_path as a file object in "write" mode ('w')
# Write a header line and write the contents of 'text' to the file
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {Total_Months}\n")
    file.write(f"Total: ${Total}\n")
    file.write(f"Average Change ${Avaerage_Change_in_Profit_Loss:.2f}\n")
    file.write(f"Greatest Increase in Profits: {Greatest_Increase_in_Profits_Month} (${Greatest_Increase_in_Profits})\n")
    file.write(f"Greatest Decrease in Profits: {Greatest_Decrease_in_Profits_Month} (${Greatest_Decrease_in_Profits})\n")