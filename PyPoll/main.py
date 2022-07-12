# Import the required modules OS helps in creating file paths across the operating system
import os
import csv

# Create variables 
total_votes = 0
candidate_name= 'String'
county = 'String'
votes_countywide = 0
county_list = []
candidate_list = []
candidate_votes = {}
county_votes = {}
candidate_results = {} 
winning_summary = {}
total_results ={}
votes = 0
winning_count = 0
vote_percentage = 0.000
winning_percentage = 0.000
winning_candidate  = 'string'
    

#Specify the path and put it in the variable csv_path
csvpath = os.path.join('.','Resources','election_data.csv')

# Open the csv file in the csv_path and load it into budget_data_file
with open(csvpath, "r") as election_data_file:
        
#  Move the budget_data_file to cvsreader
  csvreader = csv.reader(election_data_file, delimiter=',')

  # Skip the header
  next(election_data_file, None)
  
  # Loop through each line in the file

  for row in csvreader:

 # Count the total number of votes
    total_votes += 1

   #Copy the candidate name in the variable candidate_name
    candidate_name = row[2]

    # If it is a new candidate 
    if candidate_name not in  candidate_list:

    #Add to the list of candidates
     candidate_list.append(candidate_name)

    #Initialize the candidate votes
     candidate_votes[candidate_name]= 0
     
   # If the cabdidate remains the same, add another vote to the candidate 
    candidate_votes[candidate_name] += 1

   # Move the county to the variable county
    county = row[1]
 
   # If the county is new and it's not in the county list, add it to the county list
    if (county not in county_list):

      county_list.append(county)

    # Initialize the varibles that contains the votes of that particular county 
      county_votes[county] = 0

 # Add to the totals for the county
  county_votes[county] += 1
  
 # Format the results for total votes cast
  total_results= ( f"\n"
                            f"Election Results \n"
                             f"---------------------------- \n"
                             f"Total votes : {total_votes}\n"
                             f"---------------------------- \n")

# Print the Total votes to the terminal                            
  print(total_results)

 # Join the path to the file output.txt 
  docx_path = os.path.join('.','Analysis','output.txt')

 # With the path to the text file open the text file and write the total results
  with open(docx_path, "w") as f:

        f.write(total_results)

  # Calculate each candidate's vote percentage 
  for candidate_name in candidate_votes:

        votes = candidate_votes.get(candidate_name)

        vote_percentage = float(votes)/ float(total_votes) * 100
        
# Format results for each candidate
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes:,})\n")

    # Print the results for each candidate    
        print(candidate_results)  

    
        #docx_path = os.path.join('.','Analysis','output.txt')
# Open the file in the docx_path and append it with the results of each candidate
        with open(docx_path, "a") as f:
          f.write(candidate_results)

      
# Calculte which candidate has the most votes and declare the winner
        if (votes > winning_count) and (vote_percentage > winning_percentage) :
         
         winning_count = votes
         winning_candidate = candidate_name 
         winning_percentage = vote_percentage

        winning_summary = (f"-------------------------------\n"
                        f"Winner: {winning_candidate}\n"
                        f"-------------------------------\n"
                        )

 # Print the winner to the terminal
  print(winning_summary)

 # Append the text file with the winner
  with open(docx_path, "a") as f:
          f.write(winning_summary)
 