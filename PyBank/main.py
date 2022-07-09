# Import the required modules OS helps in creating file paths across the operating system

import os
import csv
total_months = 0
total_revenue = 0.0


#net_profit_loss = 0.0

# Specify the path and put it in the variable csv_path
csvpath = os.path.join('.','Resources','budget_data.csv')

# Open the csv file in the csv_path and load it into csv_file
with open(csvpath, "r") as budget_data_file:
        
  csvreader = csv.reader(budget_data_file, delimiter=',')
  #csvreader = csv.reader(budget_data_file)
  next(budget_data_file, None)

  for row in csvreader:
      total_months = total_months + 1
      net_profit_loss = row[1]
      
      total_revenue = total_revenue + float(net_profit_loss)

  currency_total_revenue = "${:.2f}".format(total_revenue)
  

 # currency_total_revenue = "${:,2f}".format(total_revenue)
  #currency_average_change = "${:.2f}".format(average_change)
       
print(f"Total number of months = ", total_months)
print(f"Total revenue = ",currency_total_revenue ) 

