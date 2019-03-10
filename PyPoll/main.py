import os
import csv

# Path to collect data from the Resources folder
voters = os.path.join('.', 'election_data.csv')

with open(voters, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header for calculations
    header = next(csvreader)
    
    # Initialization of variables
    Khan = 0
    Khan_P = 0
    Correy = 0
    Correy_P = 0
    Li = 0
    Li_P = 0
    Tooley = 0
    Tooley_P = 0
    Total_V = 0
    Winner = ' '

    # Review all the calculations    
    for row_v in csvreader:
        
        # Getting totals per candidate
        Total_V = Total_V + 1
        if(row_v[2] == 'Khan'):
            Khan = Khan + 1
        elif(row_v[2] == 'Correy'):
            Correy = Correy + 1
        elif(row_v[2] == 'Li'):
            Li = Li + 1            
        elif(row_v[2] == "O'Tooley"):
            Tooley = Tooley + 1

            # Validation for who is the winner       
    if(Khan > Correy and Khan > Li and Khan > Tooley):
        Winner = 'Khan'
    elif(Correy > Li and Correy > Tooley):
        Winner = 'Correy'
    elif(Li > Tooley):
        Winner = 'Li'
    else:
        Winner = "O'Tooley"
    
    # Getting percentage
    Khan_P = (Khan / Total_V) * 100
    Correy_P = (Correy / Total_V) * 100
    Li_P = (Li / Total_V) * 100
    Tooley_P = (Tooley / Total_V) * 100  

    lines = "Election Results\r\n"
    lines += "-------------------------\r\n"
    lines += f"Total Votes: ' + str(Total_V)\r\n"
    lines += "-------------------------\r\n"
    lines += f"Khan: {Khan_P} %{Khan}\r\n"
    lines += f"Correy: {Correy_P} %{Correy}\r\n"
    lines += f"Li: {Li_P} %{Li}\r\n"
    lines += f"O'Tooley: {Tooley_P} %{Tooley}\r\n"
    lines += "-------------------------\r\n"
    lines += f"Winner: {Winner}\r\n"
    lines += "-------------------------\r\n"

    print(lines)

# Specify the file to write to
output_path = os.path.join(".", "Votes.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file:
    text_file.write(lines) 