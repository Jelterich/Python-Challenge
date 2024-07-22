import csv
import os

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Define the file path
file_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')
print("File Path:", file_path)

# Initialize variables
total_votes = 0
candidates = {}
candidate_list = []

# Read the CSV file
with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row

    for row in reader:
        if len(row) == 0:
            continue  # Skip empty rows
        
        # Extract candidate name from the row
        candidate_name = row[2]
        
        # Update total votes
        total_votes += 1
        
        # Update candidate vote count
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Calculate required metrics
results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

winner = ""
winner_votes = 0

for candidate in candidates:
    votes = candidates[candidate]
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"
    
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

results += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print and save the results
print(results)

with open(os.path.join("PyPoll", "analysis", "results.txt"), "w") as txt_file:
    txt_file.write(results)
