# Import the required modules OS helps in creating file paths across the operating system
import os
import csv

# Create variables 
total_months = 0
total_net = 0.0
prev_net = 0.0
curr_net = 0.0
net_change = 0.0
total_revenue = 0.0
month_i = ""
month_decrease = ""
month = ""
change_in_first_row = 0.0
total_change = 0.0
first_row_net = 0.0
sum_net_change = 0.0
i = 0
increase = 0.0
decrease = 0.0
average1 = 0.0
lines = {}                   # Create a dictionary called lines

#Specify the path and put it in the variable csv_path
csvpath = os.path.join('.','Resources','budget_data.csv')

# Open the csv file in the csv_path and load it into budget_data_file
with open(csvpath, "r") as budget_data_file:
        
#  Move the budget_data_file to cvsreader
  csvreader = csv.reader(budget_data_file, delimiter=',')
  
  # Skip the header
  next(budget_data_file, None)
  
 
  # Loop through each row of the csvreader 
  for row in csvreader:
     # Add the total number of months
      total_months += 1

      # Move the value in the 2nd column to current net
      curr_net = float(row[1])

     # Move the value in the 1st column to month
      month = row[0]

      # Add the current net to the total net
      total_net += curr_net
       
      # Calculate the Net change from the previous row
      net_change = curr_net - prev_net

      # Add the net change to total net chnage
      sum_net_change += net_change

      # Add the current revenue in the first row to a variable first_row_net     
      if i == 0:
        first_row_net = curr_net
        i += 1
    
     # Compare the previous change to the current change

    # If it is lesser than the greatest decrease, make it the greatest decrease, add the corresponding month to month_decrease
      if (decrease > net_change) :
    
        decrease = net_change 
        month_decrease = month

     # Or if it is greater than the greatest increase, make it the greatest increase, add the corresponding month to month_i
      elif (increase < net_change) :
        increase = net_change   
        month_i = month
      
      # Lastly add the current revenue to the previous revenue before exiting the loop
      prev_net = float(row[1])


# The sum of net changes should not contain 1 st row, as it's not a comparison
sum_net_change = sum_net_change - first_row_net


# The average is for one less than the total months as we have not considered the first row
average1 = (sum_net_change / (total_months - 1))


# Convert the revenues to currency format
currency_total_revenue = "${:.2f}".format(total_net)       
currency_increase      = "${:.2f}".format(increase) 
currency_decrease      = "${:.2f}".format(decrease) 
currency_average       = "${:.2f}".format(average1) 

# Print to the terminal

print("")
print("Financial Analysis")
print("------------------------------")
print(f"Total number of months: ", total_months)
print(f"Total revenue: ",currency_total_revenue ) 
print(f"Average Change: ", currency_average)
print(f"Greatest Increase in Profits: ", month_i ,currency_increase)
print(f"Greatest Decrease in Profits: ", month_decrease, currency_decrease)

# Write into the csv file in in the Analysis folder
docx_path = os.path.join('.','Analysis','output.txt')

# Define a dictionary that contains explanations and variables   
lines = {'Total number of months': total_months, 
        "Total revenue: ":currency_total_revenue, "Average Change ": currency_average,
        "Greatest Increase in Profits ": [month_i , currency_increase],
        "Greatest Decrease in Profits ": [month_decrease, currency_decrease]}

# Open the output file and write the heading and the the dictonary

with open(docx_path, "w") as f: 
    
    f.write("Financial Analysis: " + '\n')
    f.write ( repr(lines) + '\n')
